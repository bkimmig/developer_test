from flask import Blueprint

mod = Blueprint(
    'main_app', __name__, url_prefix="")

## load the blueprints/routes
from .views import home
from .views import album_view
