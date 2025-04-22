# 📱 Spam SMS Detection App (Flask + ML)

## 🔍 Overview
This is a simple web-based application that detects whether an SMS is **Spam** or **Not Spam** using a trained **Multinomial Naive Bayes** classifier. The project includes data preprocessing, model training, and deployment with **Flask**.

---

## ✅ Key Features
- Clean and preprocess text using regex
- Train a spam classifier using **Multinomial Naive Bayes**
- Feature extraction with **CountVectorizer**
- Flask web app to input and classify messages
- Pre-trained model and vectorizer saved via `joblib`

---

## 📊 Dataset
- **Source**: [UCI SMS Spam Collection Dataset](https://archive.ics.uci.edu/ml/datasets/sms+spam+collection)
- ~5,500 labeled SMS messages (`ham` = not spam, `spam` = spam)

---

## 🧠 Model Pipeline
1. Load and preprocess data from `spam.csv`
2. Clean messages using regex
3. Convert text to numerical features using **CountVectorizer**
4. Train/test split (80/20)
5. Train model using **MultinomialNB**
6. Save the model and vectorizer (`model.pkl`, `vectorizer.pkl`)
7. Use Flask (`app.py`) for deployment and prediction

---

## 🛠️ Tech Stack
- **Python**
- **Flask** (for the web interface)
- **pandas**, **numpy** (data handling)
- **scikit-learn** (ML algorithms and tools)
- **joblib** (model serialization)

---

## 🚀 How to Run

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Train model** (if not already trained)
   ```bash
   python spam_model.py
   ```

3. **Run the app**
   ```bash
   python app.py
   ```

4. **Open in browser**
   ```
   http://127.0.0.1:5000/
   ```

---

## 📁 Project Structure
```
├── app.py                # Flask web app
├── spam_model.py         # Data preprocessing + model training
├── spam.csv              # Dataset
├── model.pkl             # Trained spam detection model
├── vectorizer.pkl        # Fitted CountVectorizer
├── requirements.txt      # Python dependencies
├── templates/
│   └── index.html        # HTML form (not included here)
└── README.md             # Project overview
```

---

## 🤖 Example Usage
- Input: “Congratulations! You've won a free vacation.”  
  Output: 🚫 Spam

- Input: “Can we reschedule our meeting to 3 PM?”  
  Output: ✅ Not Spam

---

## 📌 Short Description
An ML-powered app for SMS filtering.