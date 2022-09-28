import os
import sys
import pytmx
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

current_level = 0

levels = [
    Level(os.path.join('./art/Tiled', 'tutorialMap.tmx')),
]

while run:
    levels[current_level].run()
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit(0)
