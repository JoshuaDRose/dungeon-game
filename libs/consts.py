import os
import pygame

if not pygame.get_init(): pygame.init();

FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

caption = "Dungeon Explorer"
font = pygame.font.SysFont(
       os.path.join('./data', 'SCRUBLAND.ttf'),
       55, 1, 0)

img_root = ...

ACC = 0.3
FRIC = -0.10
COUNT = 0

def center_surface(a: pygame.Rect, b: pygame.Rect, c=(0, 0)) -> tuple:
    if c[0] and c[1]:
        return (a.width // 2 - b.width // 2, a.height // 2 - b.height // 2)
    elif c[0]:
        return (a.width // 2- b.width // 2)
    elif c[1]:
        return (a.height / 2- b.height // 2)
