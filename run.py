from millers_app import create_app

# Create the Flask app instance
app = create_app()

# Entry point for running the app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

