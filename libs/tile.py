import pygame
from .consts import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, image, position: float, groups: tuple):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
