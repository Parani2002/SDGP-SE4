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
    #Get values from form
    init_features=[int(x) for x in request.form.values()]
    print(init_features)

    #fit the Y values to label encoder
    transformed_data = label_encoder.fit_transform(dataset['Course'].unique())
    print(transformed_data)

    #input the values to ML Model
    prediction = model.predict([init_features])
    print(prediction)
    
    #Label Encoding for prediction
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







