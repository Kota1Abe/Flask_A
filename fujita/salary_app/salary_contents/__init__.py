from flask import Flask
app=Flask(__name__)
app.config.from_object('salary_contents.config')
import salary_contents.views