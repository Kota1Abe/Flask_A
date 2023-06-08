from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("myapp.config")

db = SQLAlchemy(app)

from myapp.views import career, views