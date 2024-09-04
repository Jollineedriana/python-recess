# millers_app/models/product.py

from millers_app.extensions import db
from millers_app.Models.order import order_products  


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    price = db.Column(db.Float, nullable=False)
    quantity_available = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(200), nullable=True)
    organic_certification = db.Column(db.String(200), nullable=True)
    nutritional_information = db.Column(db.String(500), nullable=True)
    packaging_size = db.Column(db.String(50), nullable=True)
    grain_type = db.Column(db.String(50), nullable=True)
    milling_process = db.Column(db.String(50), nullable=True)

    orders = db.relationship('Order', secondary=order_products, back_populates='products')

    def __init__(self, name, price, quantity_available, description=None, image=None, organic_certification=None, nutritional_information=None, packaging_size=None, grain_type=None, milling_process=None):
        self.name = name
        self.description = description
        self.price = price
        self.quantity_available = quantity_available
        self.image = image
        self.organic_certification = organic_certification
        self.nutritional_information = nutritional_information
        self.packaging_size = packaging_size
        self.grain_type = grain_type
        self.milling_process = milling_process

    def __repr__(self):
        return f'<Product {self.name}>'





# from millers_app.extensions import db

# class Product(db.Model):
#     __tablename__ = 'products'
    
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     description = db.Column(db.String(500))
#     price = db.Column(db.Float, nullable=False)
#     quantity_available = db.Column(db.Integer, nullable=False)
#     image = db.Column(db.String(200))
#     organic_certification = db.Column(db.String(200))
#     nutritional_information = db.Column(db.String(500))
#     packaging_size = db.Column(db.String(50))
#     grain_type = db.Column(db.String(50))
#     milling_process = db.Column(db.String(50))

#     orders = db.relationship('Order', secondary='order_products', back_populates='products')

#     def __init__(self, name, description, price, quantity_available, image=None, organic_certification=None, nutritional_information=None, packaging_size=None, grain_type=None, milling_process=None):
#         self.name = name
#         self.description = description
#         self.price = price
#         self.quantity_available = quantity_available
#         self.image = image
#         self.organic_certification = organic_certification
#         self.nutritional_information = nutritional_information
#         self.packaging_size = packaging_size
#         self.grain_type = grain_type
#         self.milling_process = milling_process

#     def __repr__(self):
#         return f'<Product {self.name}>'