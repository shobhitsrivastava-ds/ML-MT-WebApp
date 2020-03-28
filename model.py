from app import db


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    password = db.Column(db.String(60),unique=True,nullable=False)

    def __repr__(self):
        return("Name-(%s) email-{%s}"%(self.name,self.email))

class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    disease=db.Column(db.String(20),nullable=False)
    def __repr__(self):
        return("User Disease-(%s)"%(self.disease))