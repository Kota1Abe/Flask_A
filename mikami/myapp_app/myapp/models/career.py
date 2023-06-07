from myapp import db
from datetime import date, datetime

class Career(db.Model):
    __tablename__ = 'myapp_career'
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("myapp_user.id"))

    created_at = db.Column(db.DateTime)

    name = db.Column(db.String(50))
    position = db.Column(db.String(200))
    imgsrc = db.Column(db.String(200))
    s_date = db.Column(db.Date)
    
    def __init__(self, user_id=None ,name=None, position=None, imgsrc=None, s_date=None):
        self.name = name
        self.user_id = user_id
        self.position = position
        self.imgsrc = imgsrc
        self.s_date = s_date
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return "<Entry user:{} password:{}>".format(self.id, self.title, self.text)