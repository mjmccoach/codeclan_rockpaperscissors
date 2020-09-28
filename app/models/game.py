from app.models.player import Player

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play(self, player1, player2):
   
        if player1.choice == "Paper" and player2.choice == "Rock":
            return player1.name + " wins with " + player1.choice + "!"
        elif player1.choice == "Scissors" and player2.choice == "Paper":
            return player1.name + " wins with " + player1.choice + "!"
        elif player1.choice == "Rock" and player2.choice == "Scissors":
            return player1.name + " wins with " + player1.choice + "!"
        elif player1.choice == player2.choice:
            return None
        else:
            return player2.name + " wins with " + player2.choice + "!"
