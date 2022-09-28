import pygame
from .util import *
from .consts import *

class Player(pygame.sprite.Sprite):
    def __init__(self, image, position, groups):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.position = pygame.math.Vector2(self.rect.x, self.rect.y)
