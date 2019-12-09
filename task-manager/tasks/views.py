from flask import render_template
from . import tasks


@tasks.route('/', defaults={'page': 'index'})
def home(page):
    return render_template('tasks/index.html', name='Clayton Herbst', title="Task Pool")