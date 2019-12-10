import click

def register(app, db):
    @app.cli.group('db')
    def sqlite():
        pass
    
    @sqlite.command('init')
    def init_db():
        db.create_all()
    
    @sqlite.command('drop')
    def drop_tables():
        db.drop_all()
