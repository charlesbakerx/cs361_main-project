from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Recipe(db.Model):
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