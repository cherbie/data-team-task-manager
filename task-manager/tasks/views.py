from flask import Blueprint, abort, render_template

tasks = Blueprint('tasks', __name__, template_folder='templates', url_prefix='/tasks')

@tasks.route('/', defaults={'page': 'index'})
def home(page):
    return render_template('tasks/index.html', name='Clayton Herbst', title="Task Pool")