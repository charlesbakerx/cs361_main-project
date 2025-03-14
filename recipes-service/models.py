from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Recipes(db.Model):
    __tablename__ = 'Recipes'
    Recipe_ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100), nullable=False)
    Instructions = db.Column(db.String(1000), nullable=False)
    Description = db.Column(db.String(1000), nullable=True)

    def to_dict(self):
        return {
            'Recipe_ID': self.Recipe_ID,
            'Name': self.Name,
            'Instructions': self.Instructions,
            'Description': self.Description
        }

class Ingredients(db.Model):
    __tablename__ = 'Ingredients'
    Item_ID = db.Column(db.Integer, db.ForeignKey('Items_In_House.Item_ID'), primary_key=True)
    Recipe_ID = db.Column(db.Integer, db.ForeignKey('Recipes.Recipe_ID'), primary_key=True)

    def to_dict(self):
        return {
            'Recipe_ID': self.Recipe_ID,
            'Item_ID': self.Item_ID
        }