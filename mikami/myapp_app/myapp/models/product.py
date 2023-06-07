from myapp import db
from datetime import date, datetime

class Product(db.Model):
    __tablename__ = 'myapp_product'
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("myapp_user.id"))

    created_at = db.Column(db.DateTime)

    title = db.Column(db.String(50))
    imgsrc = db.Column(db.String(200))
    s_date = db.Column(db.Date)
    
    def __init__(self, user_id=None, title=None, imgsrc=None, s_date=None):
        self.user_id = user_id
        self.title = title
        self.imgsrc = imgsrc
        self.s_date = s_date
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return "<Entry user:{} password:{}>".format(self.id, self.title, self.text)