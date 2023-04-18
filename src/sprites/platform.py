import pygame
import os

path = "ot-harjoitustyo/src/sprites/"
dirname = os.path.dirname(__file__)

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width):
        super().__init__()

        self.image = pygame.image.load(os.path.join(dirname, "..", "assets", "platform.png"))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width

    def update(self, scroll):

        #moves platform down
        self.rect.y += scroll

        #deletes platform when it leaves screen
        if self.rect.y > 600:
            self.kill()