from flask import Blueprint, request, jsonify
from millers_app.extensions import db
from millers_app.Models.contact import Contact  # Assuming Contact is defined in Models.contact
from datetime import datetime

contact_bp = Blueprint('contact_bp', __name__, url_prefix='/api/v1/contact')

# Create a new contact
@contact_bp.route('/create', methods=['POST'])
def create_contact():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')
    
    if not name or not email or not message:
        return jsonify({'error': 'Missing required fields'}), 400

    new_contact = Contact(name=name, email=email, message=message)  # Instantiate Contact class
    db.session.add(new_contact)
    db.session.commit()

    return jsonify({'message': 'Contact created', 'contact_id': new_contact.id}), 201
