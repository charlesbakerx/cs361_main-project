from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from models import db, Recipe

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://cs361_bakerc22:<password>@classmysql.engr.oregonstate.edu:3306/cs361_bakerc22'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)