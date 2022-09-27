import pygame
from .util import *
from .consts import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = load_image(
                     image='../art/Tilemap/tilemap.png',
                     colorkey=WHITE,
                     root=root)
        self.rect = self.image.get_rect()
