""" Sound bar class for settings menu """

import pygame
from pygame.locals import *


class Cell(pygame.sprite.Sprite):
    """ Individual cell """
    def __init__(self, color, *groups):
        super().__init__(groups)
        self.image = pygame.Surface([25, 10], SRCALPHA)


class Bar(pygame.sprite.Sprite):
    """ Bar class for multiple cells """
    def __init__(self, color, *groups):
        super().__init__(groups)
        self.image = pygame.Surface([25 * 10, 10])
        self.cells = pygame.sprite.Group()
        for i in range(0, self.image.get_width() / 25):
            cell = Cell('#cbcbfd', self.cells)
