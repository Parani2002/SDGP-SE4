from flask import Flask
from flask import render_template,request

app = Flask(__name__)

@app.route('/')
@app.route('/home')

def home():
    return render_template('index.html')

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
    app.run(debug=True)




def index():
    return 'Hello World'