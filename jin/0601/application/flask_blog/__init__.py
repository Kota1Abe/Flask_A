from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_object('flask_blog.config') # APP . CONFIG <- FLASK_BLOG.CONFIG 

db = SQLAlchemy(app)

# import flask_blog.views

from flask_blog.views import views,entries 


