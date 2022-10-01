import pygame
from .consts import *


class Health(pygame.sprite.Sprite):
    """ UI health bar """
    def __init__(self, position, groups, health=100):
        super().__init__(groups)
        self.image = pygame.Surface((100, 20), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.health = health
        self.position = position
        self.do_init = 1 # high velocity increase

    def draw(self, surface) -> None:
        pygame.draw.rect(surface, (200, 45, 10), pygame.Rect(
            self.rect.x, self.rect.y, self.health, 20), 0, 10)


class Stamina(pygame.sprite.Sprite):
    """ Stamina UI bar """
    def __init__(self, position, groups, stamina=50):
        super().__init__(groups)
        self.image = pygame.Surface((100, 20))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.stamina = 0
        self.position = position
        self.do_init = 1 # high velocity increase

    def draw(self, surface) -> None:
        pygame.draw.rect(surface, '#6699ff', pygame.Rect(
            self.rect.x, self.rect.y, self.stamina, 20), 0, 10)
