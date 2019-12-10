import os
from read_env import read_env

basedir = os.path.abspath(os.path.dirname(__file__))
read_env()

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    PORT = os.environ.get('PORT')
    HOST = os.environ.get('HOST')
    PM_API_KEY = os.environ.get('PM_API_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {'echo': True}
