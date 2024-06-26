from flask import Flask
from flask import render_template,request,url_for,jsonify,redirect
from pymongo import *
from pymongo import MongoClient
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
import pickle
import pandas as pd
import os
import numpy as np



#Establishing MongoDB connection
cluster = MongoClient('mongodb://localhost:27017')
appdb = cluster['SDGP']
collection = appdb["Signup"]    #Signup collection


app = Flask(__name__)


#Routes
#Route for the home page
@app.route('/')
@app.route('/home')
def home():
    return render_template('main.html')

#Route for explore page
@app.route('/main')
def main():
    return render_template('home.html')


#Route for explore page
@app.route('/explore')
def explore():
    return render_template('explore.html')

#Route for newsletter page
@app.route('/news_letter')
def news_letter():
    return render_template('newsletter.html')

#Route for the questionnaire
@app.route('/questionnaire')
def questionnaire():
    return render_template('questionnaire.html')


#Route for the Signin page
@app.route('/signin_form')
def signin_form():
    return render_template('Signin.html')

#Route for the Signup page
@app.route('/signup_form')
def signup_form():
    return render_template('Signup.html')

#Route for the quiz page
@app.route('/quiz')
def quiz():
    return render_template('quiz.html')


#Route for the career page
@app.route('/career')
def career():
    return render_template('career.html')



# Load the trained model
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




# Load the dataset
path = 'Back_end/dataset1.csv'
dataset = pd.read_csv(path)


# Load the trained model
with open('Back_end/knnModel.pkl', 'rb') as f:
    model = pickle.load(f)

# Create an instance of LabelEncoder
label_encoder = LabelEncoder()




@app.route('/career_quiz', methods=['POST'])
def career_quiz():
    init_features=[int(x) for x in request.form.values()]
    print(init_features)

    transformed_data = label_encoder.fit_transform(dataset['Course'].unique())
    print(transformed_data)

    prediction = model.predict([init_features])
    print(prediction)
    
    prediction = label_encoder.inverse_transform(prediction)
    print(prediction)

    
    return render_template('prediction2.html',prediction_career = prediction[0])








#login functionality using POST method
@app.route('/login', methods=['POST'])
def loginForm():
    # Get login data from form submission
    name = request.form['name']
    password = request.form['password']

    # Check if login data exists in MongoDB
    query = {"name": name, "password": password}
    document = collection.find_one(query)
    
    if document:
        print("Login successful")
        # Redirect the user to the home page or any other desired page
        return render_template("home.html")
    else:
        print("Invalid username or password")
        # Redirect the user back to the login page or show an error message
        return redirect(url_for('signin_form'))  # Assuming you have a Signin page route




#Signup into page and mongoDB connection
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    print("connected")
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        if name and email and password:  # Check if all fields are filled
            user = {
                'name': name,
                'email': email,
                'password': password
            }
            print(user)
            collection.insert_one(user)
            
            # After successful signup, redirect the user to another page
            return render_template("home.html")
        else:
            # If any field is empty, render the signup page again
            return render_template("signup.html", error="Please fill out all fields.")
    else:
        # Handle GET request for signup page
        return render_template("signup.html")


#app run on port number 8000
#hhtp//localhost:8000
if __name__ == "__main__":
    app.run(debug=True, port=8000)


