import random
import pygame
from sprites.player import Player
from sprites.platform import Platform
from sprites.coin import Coin
import game_functions


class Game:
    """Class for handling game variables, gameloop, events and drawing screen.

    Attributes:
        display: sets display
        player: creates the player
        platforms: sprite group for platforms
        platform: creates first platform and is used for spacing platforms away from each other
        coin: is used for spacing coins away from each other
        coins: sprite group for coins
        clock: clock
        scroll: determines how much everything needs to move down based on how player advances
        gameover: if true, gameover-view is shown
        start: if true, start menu is shown
        highest: helps with determining score
        score: shows how far up player got to
        coins_collected: coins collected
        boost_timer: helps with spacing out boost platforms
    """
    def __init__(self, start=True):
        """Class constructor that sets game variables and starts game

        Args:
            start: determines whether start menu is shown 
        """

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
        self.boost_timer = 0

        self.gameloop()

    def new_game(self, start):
        """Starts new game.

        Args:
            start: determines whether start menu is shown 
        """

        Game(start)

    def gameloop(self):
        """Gameloop.
        """

        while True:
            game_functions.check_events(self)
            self.player.update()
            game_functions.check_collisions(self, self.platforms, self.coins, self.player)
            game_functions.scrolling_and_score(self)
            game_functions.check_gameover(self)
            game_functions.draw_screen(self)
            self.clock.tick(60)

if __name__ == "__main__":
    Game()
