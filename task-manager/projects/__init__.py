from flask import Blueprint

projects = Blueprint('projects', __name__, template_folder="templates", url_prefix='/projects')

from . import views

