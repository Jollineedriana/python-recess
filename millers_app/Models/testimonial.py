from millers_app.extensions import db


from datetime import datetime

class Testimonial(db.Model):
    __tablename__ = 'testimonials'
    
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    testimonial_text = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    rating = db.Column(db.Integer)

    def __init__(self, customer_name, testimonial_text, date=None, rating=None):
        self.customer_name = customer_name
        self.testimonial_text = testimonial_text
        if date is None:
            date = datetime.utcnow()
        self.date = date
        self.rating = rating

    def __repr__(self):
        return f'<Testimonial {self.customer_name}>'