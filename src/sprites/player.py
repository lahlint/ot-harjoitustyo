import os
import pygame

path = "ot-harjoitustyo/src/sprites/"
dirname = os.path.dirname(__file__)

class Player(pygame.sprite.Sprite):
    def __init__(self, p_x=170, p_y=370):
        super().__init__()

        self.image = pygame.image.load(os.path.join(dirname, "..", "assets", "blob.png"))
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y
        self.move_r = False
        self.move_l = False
        self.gameover = False
        self.past_border = False

        self.speed = 0
        #self.gravity = 1

    def move(self):
        #sideways moving
        if self.move_l and self.rect.x > 0:
            self.rect.x -= 5
        if self.move_r and self.rect.x + self.image.get_width() < 400:
            self.rect.x += 5
        #vertical moving
        gravity = 1
        if self.rect.y + self.image.get_height() < 600:
            self.speed -= gravity
        #falling off
        else:
            self.gameover = True
            self.speed = 0
        #update y position
        self.rect.y -= self.speed
        #check if player has passed scroll border
        if self.rect.y == 200:
            self.past_border = True
