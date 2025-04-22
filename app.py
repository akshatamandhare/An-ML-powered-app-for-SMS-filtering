from flask import Flask, render_template, request
import joblib
from spam_model import clean_text

app = Flask(__name__)

# Model & vectorizer load karo
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        message = request.form['message']
        if message.strip() == '':
            result = 'Please enter a message.'
        else:
            cleaned = clean_text(message)
            vectorized = vectorizer.transform([cleaned])
            prediction = model.predict(vectorized)[0]
            result = '🚫 Spam' if prediction == 1 else '✅ Not Spam'
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
