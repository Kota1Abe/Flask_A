from flask import Flask

app=Flask(__name__)
app.config.from_object("flask_blog.config")

import views.views

