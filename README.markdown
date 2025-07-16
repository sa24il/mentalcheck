# 🧠 MentalCheck

**MentalCheck** is an AI-powered web app that helps users reflect on their emotional state by analyzing the tone of their thoughts using a fine-tuned transformer model. It provides instant emotion predictions and logs results with a secure database backend.

---

## 🚀 Features

- 🧠 Emotion detection using a fine-tuned **BERTweet** model
- 🌐 Interactive **Flask-based web interface**
- 📊 Visual emotion trends with analytics (MongoDB + frontend ready)
- 📝 Logs each prediction with **timestamp** and **text input**
- 🔐 Simple user **authentication system**
- ☁️ Model deployed locally (can be adapted to cloud/production)

---

## 📦 Tech Stack

- Python, Flask, HTML/CSS
- Hugging Face Transformers (BERTweet)
- MongoDB (via PyMongo)
- Jinja2 templates
- Git & GitHub for version control

---

## 🧪 Emotion Categories

The app detects one of the following emotions:

- 😄 Joy  
- 😢 Sadness  
- 😨 Fear  
- 😠 Anger  
- 😐 Neutral  
- 😞 Depressed 

---

## 📸 Screenshots

> *(Insert UI screenshots here if available)*

---

## 📂 Folder Structure

```
MentalCheck/
├── app/
│   ├── __init__.py         # Flask app initialization
│   ├── routes.py           # Flask routes for web interface
│   ├── models.py           # Database models (MongoDB)
│   ├── templates/          # HTML templates (Jinja2)
│   │   ├── index.html
│   │   ├── login.html
│   │   └── dashboard.html
│   ├── static/             # CSS, JS, and other static files
│   │   ├── css/
│   │   └── js/
├── scripts/
│   ├── train_model.py      # BERTweet model training script
│   ├── predict.py          # Inference script for emotion detection
├── data/
│   ├── dataset.csv         # Training dataset (if applicable)
│   ├── pretrained_model/   # Fine-tuned BERTweet model weights
├── config/
│   ├── config.py           # Configuration (DB, model paths, etc.)
├── tests/
│   ├── test_routes.py      # Unit tests for Flask routes
│   ├── test_model.py       # Unit tests for model predictions
├── requirements.txt         # Python dependencies
├── README.md               # This file
└── run.py                  # Entry point to run the Flask app
```

---

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/username/MentalCheck.git
   cd MentalCheck
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up MongoDB**:
   - Install MongoDB locally or use a cloud instance (e.g., MongoDB Atlas).
   - Update the database connection string in `config/config.py`.

5. **Download the pre-trained model**:
   - Download the fine-tuned BERTweet model weights and place them in `data/pretrained_model/`.
   - Alternatively, run `scripts/train_model.py` to fine-tune the model (requires dataset).

6. **Run the app**:
   ```bash
   python run.py
   ```
   - Open `http://localhost:5000` in your browser.

---

## 🔧 Usage

1. **Sign Up / Log In**:
   - Create an account or log in using the authentication system.
   
2. **Input Text**:
   - Enter your thoughts or a short text in the input field.
   
3. **Get Predictions**:
   - The app will analyze the text and return the detected emotion (e.g., Joy, Sadness).
   
4. **View Trends**:
   - Check your emotion history and trends in the dashboard.

---

## 🧑‍💻 Development

- **Training the Model**:
   - Use `scripts/train_model.py` to fine-tune the BERTweet model.
   - Ensure you have a labeled dataset in `data/dataset.csv`.

- **Testing**:
   - Run unit tests with:
     ```bash
     pytest tests/
     ```

- **Adding Features**:
   - Extend `app/routes.py` for new endpoints.
   - Update `app/templates/` for new UI components.
   - Add analytics visualizations in `app/static/js/`.

---

## 🌍 Deployment

To deploy the app to a production environment:
1. Use a WSGI server like **Gunicorn**:
   ```bash
   gunicorn --bind 0.0.0.0:8000 run:app
   ```
2. Deploy to a cloud platform (e.g., Heroku, AWS, or Render).
3. Ensure MongoDB is accessible and secure (use environment variables for sensitive data).
4. Optimize the BERTweet model for inference (e.g., quantization for faster predictions).

---

## 🤝 Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.


---

## 📬 Contact

For questions or feedback, reach out via [sahilpamin018@gmail.com](sahilpamin018@gmail.com) or open an issue on GitHub.
