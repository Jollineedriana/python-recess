from flask import Blueprint, request, jsonify
from millers_app.extensions import db
from millers_app.Models.recipe import Recipe  # Adjust the import to match your model class name

recipe_bp = Blueprint('recipe_bp', __name__, url_prefix='/api/v1/recipe')

@recipe_bp.route('/recipes', methods=['POST'])
def create_recipe():
    data = request.get_json()

    # Extract data from JSON payload
    title = data.get('title')
    ingredients = data.get('ingredients')
    instructions = data.get('instructions')
    author = data.get('author')
    cooking_time = data.get('cooking_time')
    difficulty_level = data.get('difficulty_level')
    image = data.get('image')

    # Validate required fields
    if not title or not ingredients or not instructions:
        return jsonify({'error': 'Title, ingredients, and instructions are required fields'}), 400

    try:
        # Create new recipe object
        new_recipe = Recipe(
            title=title,
            ingredients=ingredients,
            instructions=instructions,
            author=author,
            cooking_time=cooking_time,
            difficulty_level=difficulty_level,
            image=image
        )

        # Add new recipe to database session and commit changes
        db.session.add(new_recipe)
        db.session.commit()

        # Return success response with recipe ID
        return jsonify({'message': 'Recipe created', 'recipe_id': new_recipe.id}), 201

    except Exception as e:
        # Handle any exceptions, rollback database changes and return error response
        db.session.rollback()
        return jsonify({'error': 'Failed to create recipe', 'details': str(e)}), 500
