from flask import Flask
from init.confing import Config
from init.startup import start

# Create an instance of the Config class to manage configurations.
config = Config()

# Initialize a Flask application instance.
app = Flask(__name__)

# Call the start function to perform additional app setup.
start(app)