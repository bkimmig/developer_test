from flask import Flask

# Define the WSGI application object
app = Flask(__name__)

app.config.from_object('config')


# ########################################################################## #
## blueprints, set up the routes
from app.main_app import mod as main_mod

app.register_blueprint(main_mod)