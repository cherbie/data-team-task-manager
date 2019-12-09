import os
from flask import Flask
from flas_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)

    from .tasks import tasks
    from .projects import projects
    app.register_blueprint(tasks)
    app.register_blueprint(projects)

    if __name__ == '__main__':
        app.run(host=config_class.HOST, port=config_class.PORT, debug=True)
    
    return app