# millers_app/controllers/customer_controllers.py
# from flask import Blueprint, request, jsonify,heck_password_hash
# from millers_app.extensions import db
# from millers_app.Models.customer import Customer

# customer_bp = Blueprint('customer_bp', __name__, url_prefix='/api/v1/customer')

# # Create a new customer
# @customer_bp.route('/customers', methods=['POST'])
# def create_customer():
#     data = request.get_json()
#     name = data.get('name')
#     email = data.get('email')
#     shipping_address = data.get('shipping_address')
#     billing_address = data.get('billing_address')
#     payment_information = data.get('payment_information')
    
#     if not name or not email:
#         return jsonify({'error': 'Name and email are required fields'}), 400
    
#     if Customer.query.filter_by(email=email).first():
#         return jsonify({'error': 'Email already exists'}), 400

#     new_customer = Customer(name=name, email=email, shipping_address=shipping_address, billing_address=billing_address, payment_information=payment_information)
#     db.session.add(new_customer)
#     db.session.commit()

#     return jsonify({'message': 'Customer created', 'customer': new_customer.id}), 201

# # Get all customers
# @customer_bp.route('/customers', methods=['GET'])
# def get_customers():
#     customers = Customer.query.all()
#     customers_list = [{'id': c.id, 'name': c.name, 'email': c.email, 'shipping_address': c.shipping_address, 'billing_address': c.billing_address, 'payment_information': c.payment_information} for c in customers]
    
#     return jsonify(customers_list), 200

# # Get a single customer by ID
# @customer_bp.route('/customers/<int:id>', methods=['GET'])
# def get_customer(id):
#     customer = Customer.query.get_or_404(id)
#     customer_data = {'id': customer.id, 'name': customer.name, 'email': customer.email, 'shipping_address': customer.shipping_address, 'billing_address': customer.billing_address, 'payment_information': customer.payment_information}
    
#     return jsonify(customer_data), 200


# @customer_bp.route('/login', methods=['POST'])
# def customer_login():
#     data = request.get_json()
#     email = data.get('email')
#     password = data.get('password')

#     if not email or not password:
#         return jsonify({'error': 'Email and password are required'}), 400

#     customer = Customer.query.filter_by(email=email).first()

#     if not customer or not check_password_hash(customer.password_hash, password):
#         return jsonify({'error': 'Invalid email or password'}), 401

#     # You can generate and return a token here if using JWT for authentication
#     # Example:
#     # token = generate_token(customer.id)
#     # return jsonify({'message': 'Logged in successfully', 'token': token}), 200

#     return jsonify({'message': 'Logged in successfully', 'customer_id': customer.id}), 200


# # Update a customer by ID
# @customer_bp.route('/customers/<int:id>', methods=['PUT'])
# def update_customer(id):
#     customer = Customer.query.get_or_404(id)
#     data = request.get_json()
    
#     customer.name = data.get('name', customer.name)
#     customer.email = data.get('email', customer.email)
#     customer.shipping_address = data.get('shipping_address', customer.shipping_address)
#     customer.billing_address = data.get('billing_address', customer.billing_address)
#     customer.payment_information = data.get('payment_information', customer.payment_information)

#     if Customer.query.filter_by(email=customer.email).first():
#         return jsonify({'error': 'Email already exists'}), 400

#     db.session.commit()

#     return jsonify({'message': 'Customer updated', 'customer': customer.id}), 200

# # Delete a customer by ID
# @customer_bp.route('/customers/<int:id>', methods=['DELETE'])
# def delete_customer(id):
#     customer = Customer.query.get_or_404(id)
#     db.session.delete(customer)
#     db.session.commit()

#     return jsonify({'message': 'Customer deleted'}), 200


# from flask import Blueprint, request, jsonify
# from werkzeug.security import check_password_hash
# from millers_app import db
# from millers_app.Models import Customer

# customer_bp = Blueprint('customer_bp', __name__)

# @customer_bp.route('/login', methods=['POST'])
# def customer_login():
#     data = request.get_json()
#     email = data.get('email')
#     password = data.get('password')

#     if not email or not password:
#         return jsonify({'error': 'Email and password are required'}), 400

#     customer = Customer.query.filter_by(email=email).first()

#     if not customer or not check_password_hash(customer.password_hash, password):
#         return jsonify({'error': 'Invalid email or password'}), 401

#     # You can generate and return a token here if using JWT for authentication
#     # Example:
#     # token = generate_token(customer.id)
#     # return jsonify({'message': 'Logged in successfully', 'token': token}), 200

#     return jsonify({'message': 'Logged in successfully', 'customer_id': customer.id}), 200

# @customer_bp.route('/customers/<int:id>', methods=['PUT'])
# def update_customer(id):
#     customer = Customer.query.get_or_404(id)
#     data = request.get_json()
    
#     customer.name = data.get('name', customer.name)
#     customer.email = data.get('email', customer.email)
#     customer.shipping_address = data.get('shipping_address', customer.shipping_address)
#     customer.billing_address = data.get('billing_address', customer.billing_address)
#     customer.payment_information = data.get('payment_information', customer.payment_information)

#     if Customer.query.filter(Customer.email == customer.email, Customer.id != id).first():
#         return jsonify({'error': 'Email already exists'}), 400

#     db.session.commit()

#     return jsonify({'message': 'Customer updated', 'customer': customer.id}), 200

# @customer_bp.route('/customers/<int:id>', methods=['DELETE'])
# def delete_customer(id):
#     customer = Customer.query.get_or_404(id)
#     db.session.delete(customer)
#     db.session.commit()

#     return jsonify({'message': 'Customer deleted'}), 200


from flask import Blueprint, request, jsonify

from millers_app import db
from millers_app.Models import customer
from millers_app.Models.customer import Customer
from werkzeug.security import generate_password_hash,check_password_hash
from flask_jwt_extended import create_access_token, jwt_required
# Adjust this import based on your project structure





customers = Blueprint('customers', __name__, url_prefix='/api/v1/customers')


@customers.route('/customer', methods=['POST'])
def create_customer():
    data = request.get_json()
    
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    shipping_address = data.get('shipping_address')
    billing_address = data.get('billing_address')
    payment_information = data.get('payment_information')

    if not name or not email or not password:
        return jsonify({'error': 'Name, email, and password are required'}), 400
    
    # Check if a customer with the same email already exists
    existing_customer = Customer.query.filter_by(email=email).first()
    if existing_customer:
        return jsonify({'error': 'A customer with this email already exists'}), 400

    # Hash the password before storing it
    hashed_password = generate_password_hash(password)

    # Create a new customer object with hashed password
    new_customer = Customer(
        name=name,
        email=email,
        password=hashed_password,
        shipping_address=shipping_address,
        billing_address=billing_address,
        payment_information=payment_information
    )
    
    # Add the new customer to the database session and commit the transaction
    db.session.add(new_customer)
    db.session.commit()

    return jsonify({'message': 'Customer created successfully', 'customer_id': new_customer.id}), 201



@customers.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    customer = Customer.query.filter_by(email=email).first()

    if not customer or not check_password_hash(customer.password, password):
        return jsonify({'error': 'Invalid email or password'}), 401

    # Generate access token (example using Flask JWT Extended)
    access_token = create_access_token(identity=customer.id)

    return jsonify({'access_token': access_token}), 200
