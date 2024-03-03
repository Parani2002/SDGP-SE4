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
    return render_template('start1.html')


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


# @app.route('/signup', methods=['POST'])
# def signup():
#     data = request.get_json()
#     users = mongo.db.users
#     existing_user = users.find_one({'username': data['username']})
#     if existing_user:
#         return jsonify({'message': 'User already exists'}), 400
#     users.insert_one(data)
#     return jsonify({'message': 'User created successfully'}), 201

# @app.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     users = mongo.db.users
#     user = users.find_one({'username': data['username'], 'password': data['password']})
#     if user:
#         return jsonify({'message': 'Login successful'}), 200
#     return jsonify({'message': 'Invalid credentials'}), 401


if __name__ == "__main__":
    app.run(debug=True, port=8001)


