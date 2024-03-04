from flask import Flask
from flask import render_template,request,url_for,jsonify
from pymongo import *


cluster = MongoClient('mongodb+srv://paranitharanparani13:Parani2002@cluster0.iidblml.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
mydb = cluster['SDGP']

mycol = mydb['Users']


app = Flask(__name__)



@app.route('/')
@app.route('/home')

def home():
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

#Route for the login page
@app.route('/login', methods =["GET"])
def login():
    return render_template('login.html')

@app.route('/login', methods =['POST'])
def loginForm():
    email = request.form['email']
    password = request.form['password']

if __name__ == "__main__":
    app.run(debug=True, port=8001)


