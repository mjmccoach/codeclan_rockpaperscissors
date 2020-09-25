from app import app
from flask import render_template
from app.models.player import *

@app.route('/')
def index():
    return render_template("index.html", title = "Home" , )

