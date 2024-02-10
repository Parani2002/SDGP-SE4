from flask import Flask
from flask import render_template,request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('Homepage.html')
def index():
    return 'Hello World'