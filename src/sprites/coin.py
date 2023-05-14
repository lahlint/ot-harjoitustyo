import os
import pygame


path = "ot-harjoitustyo/src/sprites/" #pylint: disable=C0103
dirname = os.path.dirname(__file__)


class Coin(pygame.sprite.Sprite):
    """Class for coins, that player can collect.

    Attributes:
        image: coin image
        rect: rectangle, the size of the image, for collisions
        rect.x: x-coordinate of coin's rect
        rect.y: y-coordinate of coin's rect
    """

    def __init__(self, c_x, c_y):
        """Class constructor that creates a new coin.

        Args:
            c_x: x-coordinate of coin
            c_y: y-coordinate of coin
        """

        super().__init__()

        self.image = pygame.image.load(os.path.join(
            dirname, "..", "assets", "coin.png"))
        self.rect = self.image.get_rect()
        self.rect.x = c_x
        self.rect.y = c_y

    def update(self, scroll):
        """Updates coin's position accordingly and deletes coin when needed.

        Args:
            scroll: determines how much coin needs to go down depending on how player advances
        """
        self.rect.y += scroll

        if self.rect.y > 600:
            self.kill()
            