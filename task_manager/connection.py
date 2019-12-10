from . import db
from flask import g

def get_db():
    sql_db = getattr(g, 'db', None)
    if sql_db is None: # need to populate
        g.db = db
        return db
    return  sql_db

