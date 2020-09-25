from app.models.player import Player

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play(self, player1, player2):
   
        if player1.choice == "Paper" and player2.choice == "Rock":
            return player1.name + " wins with " + player1.choice + "!"
