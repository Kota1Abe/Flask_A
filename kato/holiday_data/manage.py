from flask_script import Manager
from kato.holiday_data.flask_holiday.views import app
from flask_holiday.scripts.db import InitDB

if __name__=="__main__":
    manager = Manager(app)
    manager.add_command('init_db', InitDB())
    manager.run()