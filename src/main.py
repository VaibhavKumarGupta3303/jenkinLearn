from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def home():
    return "Hello, World!"
@app.route('/other')
def other():
    return "other!"
# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)  
