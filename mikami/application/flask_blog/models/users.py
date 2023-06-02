from flask_blog import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'entries'
    name = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(50))
    created_at = db.Column(db.DateTime)

    def __init__(self, name=None, password=None):
        self.name = name
        self.password = password
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return "<Entry user:{} password:{}>".format(self.id, self.title, self.text)