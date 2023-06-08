from flask import Flask
from flask_sqlalchemy import SQLAlchemy

holiday_app=Flask(__name__)
holiday_app.config.from_object('holiday.config')

db=SQLAlchemy(holiday_app)

from holiday.views import input,list,maintenance_date