import pygame

pygame.init()
display = pygame.display.set_mode((640,480))
player = pygame.draw.rect(display, (255, 0, 0), (50, 50, 100, 100))

x = 0
y = 0
clock = pygame.time.Clock()

while True:
    display.fill((0, 0, 0))
    display.blit(player, (x, y))

    pygame.display.flip()
    x += 1
    clock.tick(60)
