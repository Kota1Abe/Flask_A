from holiday import db
from datetime import datetime

class Entry(db.Model):
    __tablename__="holiday"
    holi_date=db.Column(db.Date,primary_key=True)
    holi_text=db.Column(db.String(20)) #unique=Trueいるかも？
    

    def __init__(self,holi_date=None,holi_text=None):
        self.holi_date=holi_date
        self.holi_text=holi_text
        #self.created_at=datetime.utcnow()

    def __repr__(self):
        return '<Entry holi_date:{} holi_text:{}>'.format(self.holi_date,self.holi_text)
    
    #スライドp58のdb.session.merge(holiday)どっかに入るかも