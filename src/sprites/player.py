import os
import pygame

path = "ot-harjoitustyo/src/sprites/"
dirname = os.path.dirname(__file__)


class Player(pygame.sprite.Sprite):
    """Class for player/character.

    Attributes:
        image: character image
        rect: rectangle, the size of the image, for collisions
        rect.x: x-coordinate of rect
        rect.y: y-coordinate of rect
        move_r: determines whether player will move right
        move_l: determines whether player will move left
        gameover: if true player has fallen off screen
        past_border: player has reached border where scrolling starts 
        speed: determines speed
    """
    def __init__(self, p_x=170, p_y=370):
        """Class constructor that crates player.

        Args:
            p_x: x-coordinate of rect
            p_y: y-coordinate of rect
        """
        super().__init__()

        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "blob.png"))
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y
        self.move_r = False
        self.move_l = False
        self.gameover = False
        self.past_border = False
        self.speed = 0

    def update(self):
        """Updates players position and checks for falling off screen.
        """

        if self.move_l and self.rect.x > 0:
            self.rect.x -= 5
        if self.move_r and self.rect.x + self.image.get_width() < 400:
            self.rect.x += 5
        gravity = 1
        if self.rect.y + self.image.get_height() < 600:
            self.speed -= gravity
        else:
            self.gameover = True
            self.speed = 0
        self.rect.y -= self.speed
        if self.rect.y <= 200:
            self.past_border = True
