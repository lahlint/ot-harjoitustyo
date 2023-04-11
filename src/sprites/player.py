import pygame
import os

path = "ot-harjoitustyo/src/sprites/"
dirname = os.path.dirname(__file__)

class Player(pygame.sprite.Sprite):
    def __init__(self, x=100, y=100):
        super().__init__()

        self.image = pygame.image.load(os.path.join(dirname, "..", "assets", "blob.png"))
        self.rect = self.image.get_rect()
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.rect.x = x
        self.rect.y = y
        self.move_r = False
        self.move_l = False

        self.speed = 0
        self.gravity = 1

    def move(self):
        if self.move_l and self.rect.x > 0:
            self.rect.x -= 5
        if self.move_r and self.rect.x + self.width < 640:
            self.rect.x += 5

        if self.rect.y + self.height < 480:
            #self.rect.y -= self.speed
            self.speed -= self.gravity
        else:
            self.speed = 20
            #self.rect.y -= self.speed
        self.rect.y -= self.speed





        