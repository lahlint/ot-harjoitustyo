import unittest
from sprites.platform import Platform
from game import Game


class TestPlatform(unittest.TestCase):
    def setUp(self):
        self.platform = Platform(100,100,64)

    def test_platform_moves_down(self):
        self.platform.rect.y = 200
        self.platform.update(5)
        self.assertNotEqual(self.platform.rect.y, 200)

    def test_platform_is_deleted_after_it_leaves_screen(self):
        self.platform.rect.y = 605
        self.platform.update(0)
        self.assertTrue(self.platform, False)