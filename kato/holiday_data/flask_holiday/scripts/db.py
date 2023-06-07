from flask_script import Command
from holiday_data import db
from holiday_data.models.entries import Entry

class InitDB(Command):
    "create database"

    def run(self):
        db.create_all()