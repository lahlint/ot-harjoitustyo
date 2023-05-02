import os
import pygame

path = "ot-harjoitustyo/src/sprites/"
dirname = os.path.dirname(__file__)


class Coin(pygame.sprite.Sprite):
    def __init__(self, c_x, c_y):
        super().__init__()

        self.image = pygame.image.load(os.path.join(
            dirname, "..", "assets", "coin.png"))
        self.rect = self.image.get_rect()
        self.rect.x = c_x
        self.rect.y = c_y

    def update(self, scroll):
        self.rect.y += scroll

        if self.rect.y > 600:
            self.kill()
            