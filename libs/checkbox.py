import os
import pygame
from .consts import *
from .ui import *


class CheckBox(pygame.sprite.Sprite):
    def __init__(self, pos: tuple, groups):
        super().__init__(groups)
        self.image = pygame.image.load('./art/ui/buttonSquare_beige.png').convert_alpha()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
        self.pressed = False
        self.convert = False

    def draw(self, surface) -> None:
        surface.blit(self.image, self.rect)

    def update(self):
        if self.pressed:
            if self.convert:
                self.image = pygame.image.load('./art/ui/buttonSquare_beige_pressed.png').convert_alpha()
                self.image.set_colorkey((0, 0, 0))
                self.convert = False
        else:
            if self.convert:
                self.image = pygame.image.load('./art/ui/buttonSquare_beige.png').convert_alpha()
                self.image.set_colorkey((0, 0, 0))
                self.convert = False

    def toggle(self):
        self.convert = not self.convert
        self.pressed = not self.pressed

