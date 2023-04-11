import pygame
from sprites.player import Player
from sprites.platform import Platform
import random

class Game:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((640,480))
        self.player = Player()
        self.platforms = pygame.sprite.Group()
        self.clock = pygame.time.Clock()

        for i in range(15):
            width = random.randint(40, 60)
            x = random.randint(0, 480 - width)
            y = i * random.randint(40, 100)
            platform = Platform(x, y, width)
            self.platforms.add(platform)

        self.gameloop()

    def gameloop(self):
        while True:
            self.check_events()
            self.player.move()
            self.draw_screen()
            self.clock.tick(60)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.move_l = True
                if event.key == pygame.K_RIGHT:
                    self.player.move_r = True
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.move_l = False
                if event.key == pygame.K_RIGHT:
                    self.player.move_r = False

            if event.type == pygame.QUIT:
                exit()

        for p in self.platforms:
            if p.rect.colliderect(self.player.rect):
                if self.player.speed < 0:
                    self.player.speed = 20

    def draw_screen(self):
        self.display.fill((255, 255, 255))
        self.platforms.draw(self.display)
        self.display.blit(self.player.image, (self.player.rect.x, self.player.rect.y))
        
        pygame.display.flip()

Game()
