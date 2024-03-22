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
app = Flask(_name_)
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
#app run on port number 8000
#hhtp//localhost:8000
if _name_ == "_main_":
    app.run(debug=True, port=8000) 