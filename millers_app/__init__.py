from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from millers_app.extensions import db, migrate, jwt



# Import blueprints after app initialization
from millers_app.controllers.contact_controllers import contact_bp
from millers_app.controllers.order_controllers import order_bp
from millers_app.controllers.recipe_controllers import recipe_bp
from millers_app.controllers.product_controllers import product_bp
from millers_app.controllers.customer_controllers import customers
from millers_app.controllers.newsletter_controllers import newsletter_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize SQLAlchemy with the Flask application instance
    db.init_app(app)
    migrate.init_app(app, db)  # Initialize Flask-Migrate
    jwt.init_app(app)  # Initialize Flask-JWT-Extended

    # Import models here to avoid circular imports
    from millers_app.Models.contact import Contact
    from millers_app.Models.customer import Customer
    from millers_app.Models.newsletter import NewsletterSubscription
    from millers_app.Models.product import Product
    from millers_app.Models.recipe import Recipe
    from millers_app.Models.testimonial import Testimonial

    

    @app.route('/')
    def home():
        return "Hello programmers"
    




    # Register blueprints
    app.register_blueprint(contact_bp)     
    app.register_blueprint(order_bp)
    app.register_blueprint(recipe_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(customers, url_prefix='/api/v1/customers')
    app.register_blueprint(newsletter_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
