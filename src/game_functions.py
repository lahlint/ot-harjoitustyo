import random
import sys
import pygame
from sprites.platform import Platform
from sprites.boost_platform import BoostPlatform
from sprites.coin import Coin


def check_events(game):
    """Checks events/user interaction.

    Args:
        game: game object
    """
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.player.move_l = True
            if event.key == pygame.K_RIGHT:
                game.player.move_r = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                game.player.move_l = False
            if event.key == pygame.K_RIGHT:
                game.player.move_r = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                game.start = False
                game.new_game(False)
            if event.key == pygame.K_F2:
                game.start = True
                game.new_game(True)

        if event.type == pygame.QUIT:
            sys.exit()

def scrolling_and_score(game):
    """Handles scrolling and determines score

    Args:
        game: game object
    """
    scroll_border = 200
    if game.player.rect.y <= scroll_border:
        if game.player.speed > 0:
            game.scroll = game.player.speed
            game.player.rect.y = game.player.rect.y + game.scroll
            if game.player.past_border:
                game.score += game.scroll/60
    else:
        game.scroll = 0
        if not game.player.past_border:
            if (600-game.player.rect.y)/60 > game.highest:
                game.highest = (600-game.player.rect.y)/60
                game.score = game.highest

def check_gameover(game):
    """Checks whether player has fallen.

    Args:
        game: game object
    """
    if game.player.gameover:
        game.gameover = True

def draw_screen(game):
    """Handles drawing everything on screen.

    Args:
        game: game object
    """
    if game.gameover:
        draw_gameover_screen(game)
    elif game.start:
        draw_startmenu(game)
    else:
        draw_game(game)

    pygame.display.flip()

def draw_gameover_screen(game):
    """Handles drawing gameover-view.

    Args:
        game: game object
    """
    font1 = pygame.font.SysFont("Arial", 28)
    font2 = pygame.font.SysFont("Arial", 45)
    pygame.draw.rect(game.display, (0, 0, 0), (50, (600-210)/2, 300, 210))
    pygame.draw.rect(game.display, (255, 255, 255),
                        (55, (600-200)/2, 290, 200))
    message = font2.render("GAME OVER", True, (0, 0, 0))
    game.display.blit(message, (200-message.get_width()/2, 220))
    message = font1.render(f"SCORE: {game.score:.0f}", True, (0, 0, 0))
    game.display.blit(message, ((65, 280)))
    message = font1.render(f"COINS: {game.coins_collected}", True, (0, 0, 0))
    game.display.blit(message, ((65, 320)))
    message = font1.render("ENTER = New game", True, (0, 0, 0))
    game.display.blit(message, (65, 360))

def draw_startmenu(game):
    """Handles drawing startmenu-view.

    Args:
        game: game object
    """
    font1 = pygame.font.SysFont("Arial", 28)
    font2 = pygame.font.SysFont("Arial", 45)
    colors = [(187, 255, 255), (174, 238, 238), (150, 205, 205),
                (99, 184, 255), (79, 148, 205), (0, 154, 205)]
    game.display.fill(colors[0])
    messages = ["Platform", "jumping", "game!"]
    heights = [110, 160, 210]
    blit_messages(game, messages, heights, font2)
    messages = ["Jump as high on the", "platforms as you can!"]
    heights = [280, 320]
    blit_messages(game, messages, heights, font1)
    messages = ["Use the ARROW KEYS",
                "to move sideways.", "ENTER = start game"]
    heights = [360, 400, 440]
    blit_messages(game, messages, heights, font1)

def draw_game(game):
    """Handles drawing everything during the game.

    Args:
        game: game object
    """
    colors = [(187, 255, 255), (174, 238, 238), (150, 205, 205),
                (123, 185, 200), (79, 148, 205), (0, 154, 205), (10,115,205), (0,75,170)]
    score_tresholds = [0, 100, 300, 500, 700, 900, 1100, 1400]#[0,20,30,40,50,60,80,100]
    for i, score_treshold in enumerate(score_tresholds):
        if game.score > score_treshold:
            color = colors[i]
    game.display.fill(color)
    font1 = pygame.font.SysFont("Arial", 28)

    generate_platforms(game)
    game.platforms.update(game.scroll)
    game.platforms.draw(game.display)
    generate_coins(game)
    game.coins.update(game.scroll)
    game.coins.draw(game.display)
    game.display.blit(game.player.image,
                        (game.player.rect.x, game.player.rect.y))
    message = font1.render(f"Score: {game.score:.0f}", True, (0, 0, 0))
    game.display.blit(message, (10, 5))
    message = font1.render(f"Coins: {game.coins_collected}", True, (0, 0, 0))
    game.display.blit(message, (10, 30))
    message = font1.render("F2 = Menu", True, (0, 0, 0))
    game.display.blit(message, (400-message.get_width() - 10, 5))

def generate_platforms(game):
    """Generates platforms, regular and boost.

    Args:
        game: game object
    """
    while len(game.platforms) < 10:
        width = 64
        p_x = random.randint(0, 400 - width)
        p_y = game.platform.rect.y - random.randint(90, 120)
        game.platform = Platform(p_x, p_y, width)
        game.platforms.add(game.platform)
        game.boost_timer += 1
    if game.boost_timer == random.randint(15, 20):
        game.boost_timer = 0
        width = 64
        p_x = random.randint(0, 400 - width)
        p_y = game.platform.rect.y - random.randint(90, 120)
        game.platform = BoostPlatform(p_x, p_y, width)
        game.platforms.add(game.platform)

def generate_coins(game):
    """Generates coins.

    Args:
        game: game object
    """
    while len(game.coins) < 10:
        c_x = random.randint(0, 400 - 32)
        c_y = game.coin.rect.y - random.randint(300, 700)
        game.coin = Coin(c_x, c_y)
        game.coins.add(game.coin)

def blit_messages(game, messages, heights, font):
    """Helps with blitting multiple lines of text.

    Args:
        game: game object
        messages: list of strings
        heights: list of heights on which the messages will be placed
        font: font with font size
    """
    for i, string in enumerate(messages):
        message = font.render(string, True, (0, 0, 0))
        game.display.blit(message, (200-message.get_width()/2, heights[i]))

def check_collisions(game, platforms, coins, player):
    """Checks players collisions with platforms and coins.

    Args:
        game: game object
        platforms: platform group
        coins: coin group
        player: player object
    """
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
