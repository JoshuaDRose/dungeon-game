import pygame
from .util import *
from .consts import *
from .spritesheet import spritesheet as ss
from .sprite_strip_anim import SpriteStripAnim as ssa

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.strips = []
