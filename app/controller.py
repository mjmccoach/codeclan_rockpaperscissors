from app import app
from flask import render_template, request, redirect
from app.models.player import *
from app.models.game import *


@app.route('/')
def index():
    return render_template('index.html')    


@app.route('/result', methods = ["POST"])
def rps_game():
    
    name1 = request.form["name1"]
    choice1 = request.form["choice1"]
    name2 = request.form["name2"]
    choice2 = request.form["choice2"]

    new_game = Game(player1,player2)
    
    result = new_game.play(player1,player2)

    return render_template('result.html', result = result)