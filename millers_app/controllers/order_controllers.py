# 

# from flask import Blueprint, request, jsonify
# from millers_app.extensions import db
# from millers_app.Models.order import Order
# from millers_app.Models.product import Product

# order_bp = Blueprint('order_bp', __name__, url_prefix='/api/v1/order')

# # Create a new order
# @order_bp.route('/orders', methods=['POST'])
# def create_order():
#     data = request.get_json()
#     order_number = data.get('order_number')
#     customer_id = data.get('customer_id')
#     products_ordered = data.get('products_ordered')
#     total_amount = data.get('total_amount')
#     status = data.get('status')
#     shipping_method = data.get('shipping_method')
#     tracking_information = data.get('tracking_information')

#     if not order_number or not customer_id or not total_amount:
#         return jsonify({'error': 'Missing required fields'}), 400

#     if Order.query.filter_by(order_number=order_number).first():
#         return jsonify({'error': 'Order number already exists'}), 400

#     new_order = Order(
#         order_number=order_number,
#         customer_id=customer_id,
#         total_amount=total_amount,
#         status=status,
#         shipping_method=shipping_method,
#         tracking_information=tracking_information
#     )

#     # Adding the relationship products
#     for product_id in products_ordered:
#         product = Product.query.get(product_id)
#         if product:
#             new_order.products.append(product)

#     db.session.add(new_order)
#     db.session.commit()

#     return jsonify({'message': 'Order created', 'order_id': new_order.id}), 201

# # Get all orders
# @order_bp.route('/orders', methods=['GET'])
# def get_orders():
#     orders = Order.query.all()
#     orders_list = [{
#         'id': o.id,
#         'order_number': o.order_number,
#         'customer_id': o.customer_id,
#         'products_ordered': [p.id for p in o.products],
#         'total_amount': o.total_amount,
#         'order_date': o.order_date,
#         'status': o.status,
#         'shipping_method': o.shipping_method,
#         'tracking_information': o.tracking_information
#     } for o in orders]

#     return jsonify(orders_list), 200

# # Get a single order by ID
# @order_bp.route('/orders/<int:id>', methods=['GET'])
# def get_order(id):
#     order_obj = Order.query.get_or_404(id)
#     order_data = {
#         'id': order_obj.id,
#         'order_number': order_obj.order_number,
#         'customer_id': order_obj.customer_id,
#         'products_ordered': [p.id for p in order_obj.products],
#         'total_amount': order_obj.total_amount,
#         'order_date': order_obj.order_date,
#         'status': order_obj.status,
#         'shipping_method': order_obj.shipping_method,
#         'tracking_information': order_obj.tracking_information
#     }

#     return jsonify(order_data), 200

# # Update an order by ID
# @order_bp.route('/orders/<int:id>', methods=['PUT'])
# def update_order(id):
#     order_obj = Order.query.get_or_404(id)
#     data = request.get_json()

#     order_obj.order_number = data.get('order_number', order_obj.order_number)
#     order_obj.customer_id = data.get('customer_id', order_obj.customer_id)
#     order_obj.products_ordered = data.get('products_ordered', order_obj.products_ordered)
#     order_obj.total_amount = data.get('total_amount', order_obj.total_amount)
#     order_obj.status = data.get('status', order_obj.status)
#     order_obj.shipping_method = data.get('shipping_method', order_obj.shipping_method)
#     order_obj.tracking_information = data.get('tracking_information', order_obj.tracking_information)

#     db.session.commit()

#     return jsonify({'message': 'Order updated', 'order_id': order_obj.id}), 200

# # Delete an order by ID
# @order_bp.route('/orders/<int:id>', methods=['DELETE'])
# def delete_order(id):
#     order_obj = Order.query.get_or_404(id)
#     db.session.delete(order_obj)
#     db.session.commit()

#     return jsonify({'message': 'Order deleted', 'order_id': id}), 200


from flask import Blueprint, request, jsonify
from millers_app.extensions import db
from millers_app.Models.order import Order
from millers_app.Models.product import Product
from flask_jwt_extended import jwt_required, get_jwt_identity
order_bp = Blueprint('order_bp', __name__, url_prefix='/api/v1/order')

# Create a new order
@order_bp.route('/orders', methods=['POST'])
@jwt_required()
def create_order():
    current_user_id = get_jwt_identity()
    data = request.get_json()
    order_number = data.get('order_number')
    customer_id = data.get('customer_id')
    products_ordered_ids = data.get('products_ordered', [])  # Ensure it's a list even if single product

    # Convert total_amount from string to float
    total_amount_str = data.get('total_amount', '0').replace(',', '')  # Handle comma separators
    total_amount = float(total_amount_str) if total_amount_str.isdigit() else 0.0

    status = data.get('status', 'Pending')
    shipping_method = data.get('shipping_method')
    tracking_information = data.get('tracking_information')

    if not order_number or not customer_id or not total_amount:
        return jsonify({'error': 'Missing required fields'}), 400

    # Ensure the current user is creating an order for themselves
    # if current_user_id != customer_id:
    #     return jsonify({'error': 'Unauthorized to create order for this customer'}), 403

    if Order.query.filter_by(order_number=order_number).first():
        return jsonify({'error': 'Order number already exists'}), 400

    new_order = Order(
        order_number=order_number,
        customer_id=customer_id,
        total_amount=total_amount,
        status=status,
        shipping_method=shipping_method,
        tracking_information=tracking_information
    )

    # Handle products_ordered relationship
    for product_id in products_ordered_ids:
        product = Product.query.get(product_id)
        if product:
            new_order.products.append(product)

    db.session.add(new_order)
    db.session.commit()

    return jsonify({'message': 'Order created successfully', 'order_id': new_order.id}), 201