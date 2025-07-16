from flask import Flask, request, render_template,redirect
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from pymongo import MongoClient
from datetime import datetime
from collections import Counter
from flask_login import (
    LoginManager, login_user, logout_user,
    login_required, UserMixin, current_user
)
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # Needed for session cookies

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


# Load model + tokenizer
model_path = "fine_tuned_bertwet"
model = AutoModelForSequenceClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)
model.eval()

EMOTION_MAP = {0: "joy", 1: "sadness", 2: "fear", 3: "anger", 4: "neutral",5:"depressed"}

# Connect to MongoDB
MONGO_URI = "mongodb://localhost:27017/"  # Replace with your MongoDB URI or Atlas URI
client = MongoClient(MONGO_URI)
db = client["emotion_logs"]
collection = db["predictions"]
users_collection = db["users"]


class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


def predict_emotion(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=128)
    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=1)
        prediction = torch.argmax(probs, dim=1).item()
        return EMOTION_MAP[prediction]

@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    user = users_collection.find_one({"_id": ObjectId(current_user.id)})
    username = user["username"] if user else "User"
    if request.method == "POST":
        user_input = request.form["text"]
        emotion = predict_emotion(user_input)

        # Save to DB with user_id
        collection.insert_one({
            "user_id": current_user.id,
            "text": user_input,
            "prediction": emotion,
            "timestamp": datetime.now()
        })

        return render_template("index.html", prediction=emotion, text=user_input,username=username)
    return render_template("index.html",username=username)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        existing = users_collection.find_one({"username": username})
        if existing:
            return "Username already exists"
        users_collection.insert_one({
            "username": username,
            "password": generate_password_hash(password)
        })
        return redirect("/login")
    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = users_collection.find_one({"username": username})
        if user and check_password_hash(user["password"], password):
            login_user(User(str(user["_id"])))
            return redirect("/")
        return "Invalid credentials"
    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/login")


@app.route("/analytics")
@login_required
def analytics():
    logs = list(collection.find({"user_id": current_user.id}))
    emotions = [log["prediction"] for log in logs]
    emotion_counts = dict(Counter(emotions))
    return render_template("analytics.html", emotion_counts=emotion_counts)


# Optional: View logs
@app.route("/logs")
def view_logs():
    logs = list(collection.find().sort("timestamp", -1))
    return render_template("logs.html", logs=logs)

if __name__ == "__main__":
    app.run(debug=True)
