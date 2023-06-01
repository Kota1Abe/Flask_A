from flask import request, redirect, url_for, render_template, flash, session
from salaly import app

@app.route("/")
def show_entries():
    return "hoge"