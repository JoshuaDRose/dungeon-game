import sys
import math
import pytmx
import random
import pygame

from libs import *

pygame.init()

run = 1
clock = pygame.time.Clock()
screen_width, screen_height = 1920 // 2, 1280 // 2
screen = pygame.display.set_mode(
         (screen_width, screen_height),
         0,
         32)

ctx = {}
ctx['game'], ctx['pause'] = 1, 0

buttons = pygame.sprite.Group()
coins = pygame.sprite.Group()
tiles = pygame.sprite.Group()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # x2 buttons: "Are you sure you want to quit?" [y] [n] ...
            if ctx['game']:
                run = 0
            else:
                run = 0

        if ctx['game']:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # inversion minimizes syntax logic
                    ctx['pause'] = not ctx['pause']

    screen.fill(BLACK)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit(0)
