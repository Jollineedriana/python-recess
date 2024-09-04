# millers_app/Models/newsletter.py

from millers_app.extensions import db

class NewsletterSubscription(db.Model):
    __tablename__ = 'newsletter_subscriptions'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    subscription_date = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)

    def __init__(self, email):
        self.email = email
