import pygame
import pytmx
from .consts import *
from .spritesheet import spritesheet as ss
from .sprite_strip_anim import SpriteStripAnim as ssa

class Tile(pygame.sprite.Sprite):
    def __init__(self, image, position: float, groups: tuple):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
