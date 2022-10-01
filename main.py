#                 --  TODO  --
# - add collision to walls 
# - make player sprint function 
# - adjust player FOV only when sprinting
# - fix broken buttons
# - get player hitbox to work
# - add more levels
# - add enemy animation
# - fix ui 
# - add settings ctx
# - cool transitions? :)

import os
import sys
import pytmx
import pygame

from pygame.locals import *
from libs import *

pygame.init()

run = 1
clock = pygame.time.Clock()
screen_width, screen_height = 1920 // 2, 1280 // 2
screen = pygame.display.set_mode(
    (screen_width, screen_height),
    (HWSURFACE | DOUBLEBUF | SHOWN), 32
)
pygame.display.set_caption(caption)

current_level = 0

levels = [
    Level(os.path.join('./art/Tiled', 'tutorialMap.tmx')),
]

while run:
    levels[current_level].run()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit(0)
