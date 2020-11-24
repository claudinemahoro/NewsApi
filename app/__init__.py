from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
# bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
    

    # Creating app configurations
    app.config.from_object(config_options[config_name])

    # Initializing Flask Extensions
    # bootstrap.init_app(app)

    # Initializing Flask Extensions
    bootstrap = Bootstrap(app)
 
    # setting the config
    from .request import configure_request
    configure_request(app)

    return app