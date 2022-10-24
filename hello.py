# import the flask class from the flask module
from flask import Flask

# create an instance of the Flask class and give it the variable name 'app
app = Flask(__name__)

# create a route using the @app.route to trigger function based on endpoint
@app.route('/')
def index():
    return 'Hello, this is the index route'

# add another route
@app.route('/posts')
def posts():
    return 'posts will eventuallybe on this page'
