# from sqlalchemy import Column, Integer, String
# from database import Base

from main import db
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)
    test =db.Column(db.Integer)
    def __init__(self, id=None ,name=None, email=None):
        self.name = name
        self.email = email
        self.id =id

    # def __repr__(self):
    #     return '<User %r>' % (self.name)