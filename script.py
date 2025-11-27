import pygame
import time
import random

pygame.init()
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GREY = (120,120,120)
light = RED
pray_for_me = 0


screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
old_time = pygame.time.get_ticks()

gameRun = True
while gameRun:

    for event in pygame.event.get():
        print(event)
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            pray_for_me += 5

    new_time = pygame.time.get_ticks()
    if new_time - old_time > 5000:
        if light == RED:
             light = GREEN
        else:
            light = RED
        old_time = new_time

    pygame.draw.rect(screen, GREY,(pray_for_me,200,40,40))
    pygame.draw.rect(screen,light,(550,10,40,40))
    pygame.display.update()
    clock.tick(60)
