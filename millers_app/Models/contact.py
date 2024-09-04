from millers_app.extensions import db

from datetime import datetime

class Contact(db.Model):
    __tablename__ = 'contacts'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, name, email, message, date=None):
        self.name = name
        self.email = email
        self.message = message
        if date is None:
            date = datetime.utcnow()
        self.date = date

    def __repr__(self):
        return f'<Contact {self.name}>'
