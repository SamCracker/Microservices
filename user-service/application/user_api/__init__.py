from flask import Blueprint

user_api_blueprint = Blueprint('user-api', __name__)
from . import routes