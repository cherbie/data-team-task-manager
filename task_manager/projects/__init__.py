from flask import Blueprint

bp = Blueprint('projects', __name__, template_folder="templates", url_prefix='/projects')

from . import views

