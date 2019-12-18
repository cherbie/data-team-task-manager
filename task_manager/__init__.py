import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from .cli import register # commmand line arguments

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    from . import models
    from .connection import set_globals
    register(app, db)
    
    with app.app_context():
        set_globals(db)

    from .tasks import bp as tasks
    from .projects import bp as projects
    from .views import register_views
    app.register_blueprint(tasks)
    app.register_blueprint(projects)
    register_views(app)

    
    if __name__ == '__main__':
        app.run(host=config_class.HOST, port=config_class.PORT, debug=True)
    
    return app