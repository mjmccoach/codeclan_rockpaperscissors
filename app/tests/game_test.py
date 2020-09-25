import unittest

from app.models.game import *
from app.models.player import *

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game("Matthew","Michael")
        self.player1 = Player("Matthew","Paper")
        self.player2 = Player("Michael","Rock")
        

    def test_game(self):

        self.assertEqual("Matthew wins with Paper!", self.game.play(self.player1, self.player2))

