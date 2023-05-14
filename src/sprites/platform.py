import os
import pygame


path = "ot-harjoitustyo/src/sprites/" #pylint: disable=C0103
dirname = os.path.dirname(__file__)


class Platform(pygame.sprite.Sprite):
    """Class for regular platforms, that player can jump on.

    Attributes:
        image: platform image
        rect: rectangle, the size of the image, for collisions
        rect.x: x-coordinate of platform's rect
        rect.y: y-coordinate of platform's rect
        width: width of platform
        boost: helps differentiate between different kinds of platforms in other parts of code
    """
    def __init__(self, p_x, p_y, width):
        """Class constructor that creates new platform.

        Args:
            p_x: x-coordinate of platform
            p_y: y-coordinate of platform
            width: platfroms width
        """
        super().__init__()

        self.image = pygame.image.load(os.path.join(
            dirname, "..", "assets", "platform.png"))
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y
        self.width = width
        self.boost = False

    def update(self, scroll):
        """Updates platforms position accordingly and deletes platform when needed.

        Args:
            scroll: determines how much platform needs to go down depending on how player advances
        """
        self.rect.y += scroll
        if self.rect.y > 600:
            self.kill()
