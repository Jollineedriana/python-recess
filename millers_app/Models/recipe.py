# millers_app/Models.py

from millers_app.extensions import db

class Recipe(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=True)
    cooking_time = db.Column(db.String(50), nullable=True)
    difficulty_level = db.Column(db.String(50), nullable=True)
    image = db.Column(db.String(255), nullable=True)

    def __init__(self, title, ingredients, instructions, author=None, cooking_time=None, difficulty_level=None, image=None):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
        self.author = author
        self.cooking_time = cooking_time
        self.difficulty_level = difficulty_level
        self.image = image
