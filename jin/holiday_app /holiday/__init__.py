from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_object('holiday.config') # APP . CONFIG <- FLASK_BLOG.CONFIG 

db = SQLAlchemy(app)

# import flask_blog.views

from holiday.views import input2,list2
