from myapp import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'myapp_user'
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(50))
    career = db.relationship("Career")
    product = db.relationship("Product")

    created_at = db.Column(db.DateTime)

    text = db.Column(db.String(200))
    url = db.Column(db.String(200))
    imgsrc = db.Column(db.String(200))
    

    def __init__(self, name=None, password=None):
        self.name = name
        self.password = password
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return "<Entry user:{} password:{}>".format(self.id, self.title, self.text)