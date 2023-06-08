from holiday.__init__ import db 
# from datetime import date # datetime 도 있음
from sqlalchemy.ext.declarative import declarative_base

class Holiday(db.Model):#db.Model
    __tablename__ = "holiday"
    holi_date = db.Column(db.Date,primary_key=True)
    holi_text = db.Column(db.String(20))
   
    def __init__(self,holi_date=None,holi_text=None): # 데이터 베이스의 값을 자동으로 생성 
        self.holi_date = holi_date
        self.holi_text = holi_text
        # self.created_at = datetime.utcnow()

    def __repr__(self): # 객체의 상태를 나타낼 때 . 즉, 어떤 값이 들어갔는지 문자열로 표현 
        return '<date:{} text:{}>'.format(self.holi_date,self.holi_text)

