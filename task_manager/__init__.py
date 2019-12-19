import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from .cli import register # commmand line arguments

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # SET UP DATABASE
    db.init_app(app)
    from . import models
    from .connection import set_globals

    # REGISTER CMD
    register(app, db)
    
    # SET APP CONTEXT
    with app.app_context():
        set_globals(db)

    # SET VIEWS FOR ROUTES

    from .views import register_views
    register_views(app)

    
    if __name__ == '__main__':
        app.run(host=config_class.HOST, port=config_class.PORT, debug=True)
    
    return app