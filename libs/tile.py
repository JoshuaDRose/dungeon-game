import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, position: float, groups: tuple):
        super().__init__(groups)
        self.position: float = position
