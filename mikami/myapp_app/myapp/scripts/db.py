from flask_script import Command
from myapp import db

from myapp.models.user import User
from myapp.models.career import Career
from myapp.models.product import Product

class InitDB(Command):
    "create database"

    def run(self):
        db.create_all()