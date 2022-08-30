
from flask import Flask

app = Flask(__name__)



@app.route('/welcome')

def welcome():
    """Returns welcome in server"""

    return "welcome"



@app.route('/welcome/home')

def welcome_home():
    """Returns welcome home in server"""

    return "welcome home"



@app.route('/welcome/back')

def welcome_back():
    """Returns welcome back in server"""

    return "welcome back"