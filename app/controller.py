from app import app
from flask import render_template, request, redirect
from app.models.player import *
from app.models.game import *


@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/rules')
def result():
    return render_template('rules.html')   

@app.route('/<name1>/<choice1>/<name2>/<choice2>')
def rps_game(name1,choice1,name2,choice2):
   player1 = Player(name1, choice1)
   player2 = Player(name2, choice2)
 
   rps_game = Game(player1,player2)
 
   rps_result = rps_game.play(player1, player2)
 
   return render_template('index.html', result= rps_result)