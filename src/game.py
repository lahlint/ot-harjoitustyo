import random
import sys
import pygame
from sprites.player import Player
from sprites.platform import Platform
from sprites.boost_platform import BoostPlatform
from sprites.coin import Coin


class Game:
    def __init__(self, start=True):
        pygame.init()
        self.display = pygame.display.set_mode((400, 600))
        pygame.display.set_caption("Platform jumping game")
        self.player = Player()
        self.platforms = pygame.sprite.Group()
        self.platform = Platform(163, 560, 40)
        self.platforms.add(self.platform)
        self.coin = Coin(random.randint(0,400-32),random.randint(0,400))
        self.coins = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self.scroll = 0
        self.gameover = self.player.gameover
        self.start = start
        self.highest = 0
        self.score = 0
        self.coins_collected = 0
        self.test = False
        self.boost_timer = 0

        # starts gameloop
        self.gameloop()

    # starts a new game
    def new_game(self, start):
        Game(start)

    # starts gameloop
    def gameloop(self):
        while True:
            self.check_events()
            check_collisions(self, self.platforms, self.coins, self.player)
            self.scrolling_and_score()
            self.check_gameover()
            self.player.move()
            self.draw_screen()
            self.clock.tick(60)

    def check_events(self):
        for event in pygame.event.get():
            # check sideways arrow keys
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

            # check ENTER and F2
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.start = False
                    self.new_game(False)
                if event.key == pygame.K_F2:
                    self.start = True
                    self.new_game(True)

            # quit game
            if event.type == pygame.QUIT:
                sys.exit()


    def scrolling_and_score(self):
        # scrolling and score
        scroll_border = 200
        if self.player.rect.y <= scroll_border:
            if self.player.speed > 0:
                self.scroll = self.player.speed
                self.player.rect.y = self.player.rect.y + self.scroll
                if self.player.past_border:
                    self.score += self.scroll/60
        else:
            self.scroll = 0
            if not self.player.past_border:
                if (600-self.player.rect.y)/60 > self.highest:
                    self.highest = (600-self.player.rect.y)/60
                    self.score = self.highest

    def check_gameover(self):
        if self.player.gameover:
            self.gameover = True

    def draw_screen(self):
        if self.gameover:
            self.draw_gameover_screen()
        elif self.start:
            self.draw_startmenu()
        else:
            self.draw_game()

        pygame.display.flip()

    def draw_gameover_screen(self):
        font1 = pygame.font.SysFont("Arial", 28)
        font2 = pygame.font.SysFont("Arial", 45)
        pygame.draw.rect(self.display, (0, 0, 0), (50, (600-210)/2, 300, 210))
        pygame.draw.rect(self.display, (255, 255, 255),
                         (55, (600-200)/2, 290, 200))
        message = font2.render("GAME OVER", True, (0, 0, 0))
        self.display.blit(message, (200-message.get_width()/2, 220))
        message = font1.render(f"SCORE: {self.score:.2f}", True, (0, 0, 0))
        self.display.blit(message, ((65, 280)))
        message = font1.render(f"COINS: {self.coins_collected}", True, (0, 0, 0))
        self.display.blit(message, ((65, 320)))
        message = font1.render("ENTER = New game", True, (0, 0, 0))
        self.display.blit(message, (65, 360))

    def draw_startmenu(self):
        font1 = pygame.font.SysFont("Arial", 28)
        font2 = pygame.font.SysFont("Arial", 45)
        colors = [(187, 255, 255), (174, 238, 238), (150, 205, 205),
                  (99, 184, 255), (79, 148, 205), (0, 154, 205)]
        self.display.fill(colors[0])
        messages = ["Platform", "jumping", "game!"]
        heights = [110, 160, 210]
        self.blit_messages(messages, heights, font2)
        messages = ["Jump as high on the", "platforms as you can!"]
        heights = [280, 320]
        self.blit_messages(messages, heights, font1)
        messages = ["Use the ARROW KEYS",
                    "to move sideways.", "ENTER = start game"]
        heights = [360, 400, 440]
        self.blit_messages(messages, heights, font1)

    def draw_game(self):
        colors = [(187, 255, 255), (174, 238, 238), (150, 205, 205),
                  (99, 184, 255), (79, 148, 205), (0, 154, 205)]
        score_tresholds = [0, 100, 150, 200, 250, 300]
        for i in range(len(colors)):
            if self.score > score_tresholds[i]:
                color = colors[i]
        self.display.fill(color)
        font1 = pygame.font.SysFont("Arial", 28)

        #genereate platforms
        self.generate_platforms()
        # draw platfroms
        self.platforms.update(self.scroll)
        self.platforms.draw(self.display)
        #generate and draw coins
        self.genereate_coins()
        self.coins.update(self.scroll)
        self.coins.draw(self.display)
        #draw player
        self.display.blit(self.player.image,
                          (self.player.rect.x, self.player.rect.y))
        # shows score
        message = font1.render(f"Score: {self.score:.2f}", True, (0, 0, 0))
        self.display.blit(message, (10, 5))
        # shows collected coins
        message = font1.render(f"Coins: {self.coins_collected}", True, (0, 0, 0))
        self.display.blit(message, (10, 30))
        # shows how to get back to menu
        message = font1.render("F2 = Menu", True, (0, 0, 0))
        self.display.blit(message, (400-message.get_width() - 10, 5))

    def generate_platforms(self):
        while len(self.platforms) < 10:
            width = 64
            p_x = random.randint(0, 400 - width)
            p_y = self.platform.rect.y - random.randint(90, 120)
            self.platform = Platform(p_x, p_y, width)
            self.platforms.add(self.platform)
            self.boost_timer += 1
        if self.boost_timer == random.randint(15, 20):
            self.boost_timer = 0
            width = 64
            p_x = random.randint(0, 400 - width)
            p_y = self.platform.rect.y - random.randint(90, 120)
            self.platform = BoostPlatform(p_x, p_y, width)
            self.platforms.add(self.platform)
        
    def genereate_coins(self):
        while len(self.coins) < 10:
            c_x = random.randint(0, 400 - 32)
            c_y = self.coin.rect.y - random.randint(300, 700)
            self.coin = Coin(c_x, c_y)
            self.coins.add(self.coin)

    def blit_messages(self, messages, heights, font):
        for i in range(len(messages)):
            message = font.render(messages[i], True, (0, 0, 0))
            self.display.blit(message, (200-message.get_width()/2, heights[i]))


def check_collisions(game, platforms, coins, player):
    # check collisions between player and platforms
    for platform in platforms:
        if platform.boost and platform.rect.colliderect(player.rect):
            if player.speed < 0:
                player.speed = 45
        else:
            if platform.rect.colliderect(player.rect) and player.speed < 0:
                player.speed = 25

    for coin in coins:
        if coin.rect.colliderect(player.rect):
            coin.kill()
            game.coins_collected += 1


if __name__ == "__main__":
    Game()
