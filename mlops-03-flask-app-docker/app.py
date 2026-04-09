
# flask app for hello world

from flask import Flask      # Import the Flask class to create a web application
import numpy as np           # Import NumPy (not used here, but available for numerical operations)
import pandas as pd          # Import Pandas (not used here, but available for data handling)

app = Flask(__name__)        # Create a Flask application instance

@app.route('/', methods=['GET'])  # Define a route for the root URL that accepts GET requests
def home():                  # Define the view function for the root route
    return "Hello World"     # Return a simple text response to the client

if __name__ == "__main__":   # Check if this script is being run directly
    app.run(host="0.0.0.0", port=5000)  # Run the Flask app on all interfaces at port 5000