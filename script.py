import pygame
import random

pygame.init()

RED = (255, 0, 0)
GREEN = (0, 255, 0)
GREY = (120, 120, 120)
WHITE = (255, 255, 255)
walls = (150, 150, 124)

light = RED
pray_for_me = 0

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

old_time = pygame.time.get_ticks()
gameRun = True

while gameRun:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRun = False

    # movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        if light == RED:
            pray_for_me = 0
        elif light == GREEN:
            pray_for_me +=

    # timer update
    new_time = pygame.time.get_ticks()
    if new_time - old_time > 5000:
        # toggle light
        light = GREEN if light == RED else RED
        old_time = new_time
    if pray_for_me + 40>=600:
        screen.fill(GREEN)
        pygame.time.delay(984)
        gameRun = False

    # draw objects
    screen.fill(WHITE)
    pygame.draw.rect(screen, walls, (-25, 475, 999999, 250))
    pygame.draw.rect(screen, walls, (-25, -198, 999999, 250))
    pygame.draw.rect(screen, GREY, (pray_for_me, 200, 40, 40))
    pygame.draw.rect(screen, light, (750, 200, 40, 40))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
