import os
from . import db


class User(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True, sqlite_autoincrement=True)
    user_id = db.Column(db.String(100), unique=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    role = db.Column(db.String(150))

    def __repr__(self):
        return '<User {} {}>'.format(self.first_name, self.last_name)

class Task(db.Model):
    __tablename__ = 'Tasks'

    id = db.Column(db.Integer, primary_key=True, sqlite_autoincrement=True)
    task_id = db.Column(db.Integer, unique=True)
    project_id = db.Column(db.String(50), unique=True)
    create_date = db.Column(db.Date)
    percentage_complete = db.Column(db.Integer)
    name = db.Column(db.String(150))
    last_read_date = db.Column(db.Date)
    finish_date = db.Column(db.Date) # planned finish date
    start_date = db.Column(db.Date) # planned start date
    
    def __repr__(self):
        return '<Task id:{}, name:{}, complete:{}>'.format(self.task_id, self.name, self.percentage_complete)

class Board(db.Model):
    __tablename__ = 'Boards'
    
    id = db.Column(db.Integer, primary_key=True, sqlite_autoincrement=True)
    board_id = db.Column(db.String(100), unique=True)
    project_id = db.Column(db.String(100), unique=True)
    tasks = db.Column(db.Integer, unique=true) # one-to-many with related task id's
    groups = db.Column(db.Integer, unique=true) # one-to-many with related board group id's (cards)

    def __repr__(self):
        return '<Board id:{}, project_id:{}>'.format(self.board_id, self.project_id)

class Project(db.Model):
    __tablename__ = 'Projects'

    id = db.Column(db.Integer, primary_key=True, sqlite_autoincrement=True)
    project_id = db.Column(db.String(100))
    name = db.Column(db.String(100))
    status = db.Column(db.String(50)) # name/description of status
    priority = db.Column(db.String(100)) # name/description of prioririty

    def __repr__(self):
        return '<Project id:{}, name:{}'.format(self.id, self.name)
        

