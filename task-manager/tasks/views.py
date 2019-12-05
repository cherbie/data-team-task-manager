from flask import Blueprint, render_template_string, abort, render_template

tasks = Blueprint('tasks', __name__, template_folder='templates')

@tasks.route('/', defaults={'page': 'index'})
def home(page):
    return render_template('tasks/index.html', name='Clayton Herbst')