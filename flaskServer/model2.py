# from sqlalchemy import Column, Integer, String
# from database import e
#db是我们操作的对象
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy() 
# db.create_all()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(120))

    test =db.Column(db.Integer)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email
        

    # def __repr__(self):
    #     return '<User %r>' % (self.name)