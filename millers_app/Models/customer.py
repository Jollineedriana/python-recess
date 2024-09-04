from millers_app.extensions import db

class Customer(db.Model):
    __tablename__ = 'customers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    shipping_address = db.Column(db.String(200), nullable=False)
    billing_address = db.Column(db.String(200), nullable=False)
    payment_information = db.Column(db.String(100))
    password = db.Column(db.String(255),nullable =False)

    orders = db.relationship('Order', back_populates='customer')

    def __init__(self, name, email, password, shipping_address=None, billing_address=None, payment_information=None):
        self.name = name
        self.email = email
        self.shipping_address = shipping_address
        self.billing_address = billing_address
        self.payment_information = payment_information
        self.password = password  # Correctly assign the password attribute

    def __repr__(self):
        return f'<Customer {self.name}>'
