from flask import Blueprint

bp = Blueprint('tasks', __name__, template_folder='templates', url_prefix='/tasks')

from . import views