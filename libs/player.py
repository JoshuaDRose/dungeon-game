import pygame
from .util import *
from .consts import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.strips = []
