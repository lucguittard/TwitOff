# import the flask package to make app objects
from flask import Flask,render_template

# create the Flask web server to make the application
app = Flask(__name__)

# make a route - they determine location
@app.route("/") #for the homepage

# define a function 
def hello():
    return "Hello strange world!"


## TO RUN: FLASK_APP=hello.py flask run (in terminal)
# cannot have anyother .py files in directory


# make a template 
def home():
    return render_template('home.html')

@app.route("/about")
def preds():
    return render_template('about.html')


# another route
