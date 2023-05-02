import unittest
from sprites.player import Player
from game import Game


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player()

    def test_falling_causes_gameover(self):
        self.player.rect.y = 605
        self.player.move()

        self.assertEqual(self.player.gameover, True)

    def test_player_rect_moves_left(self):
        self.player.rect.x = 200
        self.player.move_l = True
        self.player.move()
        self.assertNotEqual(self.player.rect.x, 200)

    def test_player_rect_moves_right(self):
        self.player.rect.x + self.player.image.get_width() == 200
        self.player.move_r = True
        self.player.move()
        self.assertNotEqual(self.player.rect.x, 200)

    def test_player_past_border_is_true_after_passing_border(self):
        self.player.rect.y = 100
        self.player.move()
        self.assertEqual(self.player.past_border, True)


