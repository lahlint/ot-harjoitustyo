import unittest
from sprites.coin import Coin
from game import Game


class TestCoin(unittest.TestCase):
    def setUp(self):
        self.coin = Coin(200,200)

    def test_coin_moves_down(self):
        self.coin.update(5)
        self.assertNotEqual(self.coin.rect.y, 200)
    
    def test_coin_is_deleted_after_it_leaves_screen(self):
        self.coin.rect.y = 605
        self.coin.update(0)
        self.assertTrue(self.coin, False)
