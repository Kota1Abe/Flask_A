from flask import Flask

app = Flask(__name__)
app.config.from_object("salary.config") # .은 /와 같다 ! 

import salary.views