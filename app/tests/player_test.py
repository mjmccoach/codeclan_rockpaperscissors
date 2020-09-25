import unittest

from app.models.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("Matthew","Paper")
    
    def test_player_has_name(self):
        self.assertEqual("Matthew", self.player1.name)
