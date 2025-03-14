from types import new_class

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from models import db, Recipes, Ingredients

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://cs361_bakerc22:<password>@classmysql.engr.oregonstate.edu:3306/cs361_bakerc22'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/get_recipes', methods=['GET'])
def get_recipes():
    recipes = Recipes.query.all()
    return jsonify(recipes)

@app.route('/add_recipe', methods=['POST'])
def add_recipe(recipe_json):
    new_recipe = Recipes(Name=recipe_json.Name, Instructions=recipe_json.Instructions, Description=recipe_json.Description)
    db.session.add(new_recipe)
    db.session.commit()

@app.route('/delete_recipe', methods=['POST'])
def delete_recipe(recipe_id):
    recipe = Recipes.query.get(recipe_id)
    db.session.delete(recipe)
    db.session.commit()


db.init_app(app)