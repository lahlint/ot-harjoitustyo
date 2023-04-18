import pygame
from sprites.player import Player
from sprites.platform import Platform
import random

class Game:
    def __init__(self, start=True):
        pygame.init()
        self.display = pygame.display.set_mode((400,600))
        pygame.display.set_caption("Platform jumping game")
        self.player = Player()
        self.platforms = pygame.sprite.Group()
        self.platform = Platform(163, 560, 40)
        self.platforms.add(self.platform)
        self.clock = pygame.time.Clock()
        self.scroll_border = 200
        self.scroll = 0
        self.gameover = self.player.gameover
        self.start = start
        self.highest = 0
        self.score = 0

        #fonts
        self.font1 = pygame.font.SysFont("Arial", 28)
        self.font2 = pygame.font.SysFont("Arial", 45)

        #background colors
        self.blue1 = (187,255,255)
        self.blue2 = (174,238,238)
        self.blue3 = (150,205,205)
        self.blue4 = (99,184,255)
        self.blue5 = (79,148,205)
        self.blue6 = (0,154,205)
        self.blue8 = (0,154,205)
        
        self.gameloop()

    #starts a new game
    def new_game(self, start):
        Game(start)

    #starts gameloop
    def gameloop(self):
        while True:
            self.check_events()
            self.player.move()
            self.draw_screen()
            self.clock.tick(60)

    def check_events(self):
        for event in pygame.event.get():
            #check sideways arrow keys
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

            #check ENTER and F2
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.start = False
                    self.new_game(False)
                if event.key == pygame.K_F2:
                    self.start = True
                    self.new_game(True)


            if event.type == pygame.QUIT:
                exit()

        #check collisions between player and plratforms
        for p in self.platforms:
            if p.rect.colliderect(self.player.rect):
                if self.player.speed < 0:
                    self.player.speed = 25

        #scrolling and score
        if self.player.rect.y <= self.scroll_border:
            if self.player.speed > 0:
                self.scroll = self.player.speed
                #print(self.scroll)
                self.player.rect.y = self.player.rect.y + self.scroll
                if self.player.past_border:
                    self.score += self.scroll/60
        else:
            self.scroll = 0
            if not self.player.past_border:
                if (600-self.player.rect.y)/60 > self.highest:
                    #print("kgjvjkkjbv")
                    self.highest = (600-self.player.rect.y)/60
                    self.score = self.highest

        if self.player.gameover:
            self.gameover = True


    def draw_screen(self):

        #draw gameover window
        if self.gameover:
            pygame.draw.rect(self.display, (0, 0, 0), (50, (600-210)/2, 300, 210))
            pygame.draw.rect(self.display, (255, 255, 255), (55, (600-200)/2, 290, 200))
            self.message = self.font1.render(f"SCORE: {self.score:.2f}", True, (0, 0, 0))
            self.display.blit(self.message, ((65, 290)))
            self.message = self.font2.render(f"GAME OVER", True, (0, 0, 0))
            self.display.blit(self.message, (200-self.message.get_width()/2, 220))
            self.message = self.font1.render(f"ENTER = New game", True, (0, 0, 0))
            self.display.blit(self.message, (65, 350))

        #draw startmenu
        elif self.start:
            self.display.fill(self.blue1)
            self.message = self.font2.render(f"Platform", True, (0, 0, 0))
            self.display.blit(self.message, (200-self.message.get_width()/2, 110))
            self.message = self.font2.render(f"jumping", True, (0, 0, 0))
            self.display.blit(self.message, (200-self.message.get_width()/2, 160))
            self.message = self.font2.render(f"game!", True, (0, 0, 0))
            self.display.blit(self.message, (200-self.message.get_width()/2, 210))
            self.message = self.font1.render(f"Jump as high on the", True, (0, 0, 0))
            self.display.blit(self.message, (200-self.message.get_width()/2, 280))
            self.message = self.font1.render(f"platforms as you can!", True, (0, 0, 0))
            self.display.blit(self.message, (200-self.message.get_width()/2, 320))
            self.message = self.font1.render(f"Use the ARROW KEYS", True, (0, 0, 0))
            self.display.blit(self.message, (200-self.message.get_width()/2, 360))
            self.message = self.font1.render(f"to move sideways.", True, (0, 0, 0))
            self.display.blit(self.message, (200-self.message.get_width()/2, 400))
            self.message = self.font1.render(f"ENTER = start game", True, (0, 0, 0))
            self.display.blit(self.message, (200-self.message.get_width()/2, 440))

        #draw game
        else:

            #sets background color
            if self.score <100:
                color = self.blue1
            elif self.score <150:
                color = self.blue2
            elif self.score <200:
                color = self.blue3
            elif self.score <250:
                color = self.blue4
            elif self.score <300:
                color = self.blue5
            else:
                color = self.blue6
            self.display.fill(color)

            #generates platforms
            while len(self.platforms) < 10:
                width = 64
                x = random.randint(0, 400 - width)
                y = self.platform.rect.y - random.randint(90, 120)
                self.platform = Platform(x, y, width)
                self.platforms.add(self.platform)
            
            #draw platfroms and player
            self.platforms.update(self.scroll)
            self.platforms.draw(self.display)
            self.display.blit(self.player.image, (self.player.rect.x, self.player.rect.y))

            #shows score
            self.message = self.font1.render(f"Score: {self.score:.2f}", True, (0, 0, 0))
            self.display.blit(self.message, (10, 10))

            #shows how to get back to menu
            self.message = self.font1.render(f"F2 = Menu", True, (0, 0, 0))
            self.display.blit(self.message, (400-self.message.get_width() -10, 10))

        pygame.display.flip()

Game()
