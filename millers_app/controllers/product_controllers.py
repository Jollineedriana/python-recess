from flask import Blueprint, request, jsonify
from millers_app.extensions import db
from millers_app.Models.product import Product  # Ensure correct import path
    
product_bp = Blueprint('product_bp', __name__, url_prefix='/api/v1/product')

# Create a new product
@product_bp.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    quantity_available = data.get('quantity_available')
    image = data.get('image')
    organic_certification = data.get('organic_certification')
    nutritional_information = data.get('nutritional_information')
    packaging_size = data.get('packaging_size')
    grain_type = data.get('grain_type')
    milling_process = data.get('milling_process')
    
    if not name or not price or quantity_available is None:
        return jsonify({'error': 'Name, price, and quantity available are required fields'}), 400

    new_product = Product(
        name=name,
        description=description,
        price=price,
        quantity_available=quantity_available,
        image=image,
        organic_certification=organic_certification,
        nutritional_information=nutritional_information,
        packaging_size=packaging_size,
        grain_type=grain_type,
        milling_process=milling_process
    )

    db.session.add(new_product)
    db.session.commit()

    return jsonify({'message': 'Product created', 'product': new_product.id}), 201

# Get all products
@product_bp.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    products_list = [{
        'id': p.id,
        'name': p.name,
        'description': p.description,
        'price': p.price,
        'quantity_available': p.quantity_available,
        'image': p.image,
        'organic_certification': p.organic_certification,
        'nutritional_information': p.nutritional_information,
        'packaging_size': p.packaging_size,
        'grain_type': p.grain_type,
        'milling_process': p.milling_process
    } for p in products]
    
    return jsonify(products_list), 200

# Get a single product by ID
@product_bp.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    product_data = {
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'quantity_available': product.quantity_available,
        'image': product.image,
        'organic_certification': product.organic_certification,
        'nutritional_information': product.nutritional_information,
        'packaging_size': product.packaging_size,
        'grain_type': product.grain_type,
        'milling_process': product.milling_process
    }
    
    return jsonify(product_data), 200

# Update a product by ID
@product_bp.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.get_json()
    
    product.name = data.get('name', product.name)
    product.description = data.get('description', product.description)
    product.price = data.get('price', product.price)
    product.quantity_available = data.get('quantity_available', product.quantity_available)
    product.image = data.get('image', product.image)
    product.organic_certification = data.get('organic_certification', product.organic_certification)
    product.nutritional_information = data.get('nutritional_information', product.nutritional_information)
    product.packaging_size = data.get('packaging_size', product.packaging_size)
    product.grain_type = data.get('grain_type', product.grain_type)
    product.milling_process = data.get('milling_process', product.milling_process)

    db.session.commit()

    return jsonify({'message': 'Product updated', 'product': product.id}), 200

# Delete a product by ID
@product_bp.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()

    return jsonify({'message': 'Product deleted'}), 200
