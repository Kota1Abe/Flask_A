#DB定義
from holiday import db

class HolidayMaster(db.Model):
    __tablename__='holiday'
    holi_date=db.Column(db.DateTime,primary_key=True)
    holi_text=db.Column(db.String(20))

    def __init__(self,date=None,text=None):
        self.holi_date=date
        self.holi_text=text
        
    def __repr__(self):
        return '<date:{} text:{}>'.format(self.holi_date,self.holi_text)