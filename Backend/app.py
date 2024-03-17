from flask import Flask
from flask import render_template,request,url_for,jsonify,redirect
from pymongo import *
from pymongo import MongoClient

#Establishing MongoDB connection
cluster = MongoClient('mongodb://localhost:27017')
appdb = cluster['SDGP']
collection = appdb["Signup"]    #Signup collection


app = Flask(_name_)


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