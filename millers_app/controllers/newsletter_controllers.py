from flask import Blueprint, request, jsonify
from millers_app.extensions import db
from millers_app.Models.newsletter import NewsletterSubscription  # Adjust the import path as per your project structure

newsletter_bp = Blueprint('newsletter_bp', __name__, url_prefix='/api/v1/newsletter')

@newsletter_bp.route('/newsletters', methods=['POST'])
def create_newsletter():
    data = request.get_json()

    try:
        # Check if 'email' field is present in JSON data
        email = data.get('email')
        if not email:
            return jsonify({'error': 'Email is required'}), 400

        # Check if email is already subscribed
        existing_newsletter = NewsletterSubscription.query.filter_by(email=email).first()
        if existing_newsletter:
            return jsonify({'error': 'Email already subscribed'}), 400

        # Create new newsletter subscription
        new_newsletter = NewsletterSubscription(email=email)

        # Add new newsletter to database session and commit changes
        db.session.add(new_newsletter)
        db.session.commit()

        # Return success message with newsletter ID
        return jsonify({'message': 'Newsletter subscription created', 'newsletter_id': new_newsletter.id}), 201

    except Exception as e:
        # Handle any database errors
        db.session.rollback()
        return jsonify({'error': 'Failed to create newsletter subscription', 'details': str(e)}), 500
