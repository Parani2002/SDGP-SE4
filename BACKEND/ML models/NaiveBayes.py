# Load the trained model
import pickle
from turtle import pd

from flask import app, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer


with open('Back_end/naive_model.pkl', 'rb') as f:
    mod = pickle.load(f)

# Load the TF-IDF vectorizer
tfidf = TfidfVectorizer()

# Load the dataset
path = 'Back_end/dataset.csv'
df = pd.read_csv(path)
df = df.rename(columns={'career name': 'type of career', 'in demand for the next 10 years?': 'in demand'})
df['in demand'] = df['in demand'].map({'yes': 'in demand', 'no': 'not in demand'})
tfidf.fit(df['type of career'])

@app.route('/predict', methods=['POST'])
def predict():
    # Get input text from the HTML form
    input_text = request.form['career-input']

    # Transform input text using the TF-IDF vectorizer
    text_features = tfidf.transform([input_text])

    # Make prediction using the trained model
    prediction = mod.predict(text_features)

    # Return prediction to HTML page
    return render_template('prediction.html', prediction=prediction[0])