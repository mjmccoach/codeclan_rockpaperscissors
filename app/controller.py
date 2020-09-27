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

   choice1 = player1.name + " chose " + player1.choice + "!"
   choice2 = player2.name + " chose " + player2.choice + "!"
 
   return render_template('index.html', result= rps_result, choice1 = choice1, choice2 = choice2)

@app.route('/result', methods= ["POST"])
def play_game(name1, choice1, name2, choice2):
    
    name1 = request.form["name1"]
    choice1 = request.form["choice1"]
    name2 = request.form["name2"]
    choice2 = request.form["choice2"]

    new_game = Game(player1,player2)
    
    result = new_game.play(player1,player2)
    
    return redirect('/result.html')
    return render_template('/result.html', result = result)
    