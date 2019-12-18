from flask import g

def set_globals(db):
    def get_db():
        sql_db = getattr(g, 'db', None)
        if sql_db is None: # need to populate
            g.db = db
        return g.db

