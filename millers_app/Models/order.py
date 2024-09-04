# 

from millers_app.extensions import db
from datetime import datetime

# Define the association table
order_products = db.Table('order_products',
    db.Column('order_id', db.Integer, db.ForeignKey('orders.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('products.id'), primary_key=True)
)

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    order_number = db.Column(db.String(50), unique=True, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='Pending')
    shipping_method = db.Column(db.String(50), nullable=True)
    tracking_information = db.Column(db.String(100), nullable=True)

    customer = db.relationship('Customer', back_populates='orders')
    products = db.relationship('Product', secondary=order_products, back_populates='orders')

    def __init__(self, order_number, customer_id, total_amount, order_date=None, status=None, shipping_method=None, tracking_information=None):
        self.order_number = order_number
        self.customer_id = customer_id
        self.total_amount = total_amount
        self.order_date = order_date or datetime.utcnow()
        self.status = status or 'Pending'
        self.shipping_method = shipping_method
        self.tracking_information = tracking_information

    def __repr__(self):
        return f'<Order {self.order_number}>'
