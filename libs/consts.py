import os
import pygame

if not pygame.get_init(): pygame.init();

FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

font = pygame.font.SysFont(
       pygame.font.get_default_font(),
       55, 1, 0)

img_root = ...

ACC = 0.3
FRIC = -0.10
COUNT = 0
