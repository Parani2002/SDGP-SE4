from flask import Flask
from flask import render_template,request,url_for,jsonify,redirect
from pymongo import *
from pymongo import MongoClient


cluster = MongoClient('mongodb://localhost:27017')
appdb = cluster['SDGP']
collection = appdb["career"]