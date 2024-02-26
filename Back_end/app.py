from flask import Flask
from flask import render_template,request,url_for,jsonify
from pymongo import *


cluster = MongoClient('mongodb+srv://paranitharanparani13:Parani2002@cluster0.iidblml.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
mydb = cluster['SDGP']

mycol = mydb['Users']


app = Flask(__name__)

# @app.route('/insert')
# def insert():
#     db = cluster.get_database('SDGP')
#     collection = db['mycollection']
#     result = collection.insert_one({'name': 'John', 'age': 30})
#     return f'Inserted document with id: {result.inserted_id}'
# insert()


@app.route('/')
@app.route('/home')

def home():
    return render_template('index.html')

@app.route("/test", methods=['GET'])
def test():
    if request.method == 'GET':
        return jsonify({"response":"GET request called"})

#Route for career finder model
@app.route('/career_finder')
def career_finder():
    return render_template('career_finder.html')

#Route for the university finder
@app.route('/university_finder')
def university_finder():
    return render_template('uinversity_finder.html')

#Route for the login page
@app.route('/login', methods =["GET"])
def login():
    return render_template('login.html')

@app.route('/login', methods =['POST'])
def loginForm():
    email = request.form['email']
    password = request.form['password']

if __name__ == "__main__":
    app.run(debug=True, port=8000)




def index():
    return 'Hello World'