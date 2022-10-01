import pygame
from .consts import *


class Health(pygame.sprite.Sprite):
    """ UI health bar """
    def __init__(self, position, groups, health=100):
        super().__init__(groups)
        self.image = pygame.Surface((150, 50), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.health = health
        self.position = position

    def update(self) -> None:
        pygame.draw.rect(self.image, (200, 45, 10), pygame.Rect(
            self.rect.x, self.rect.y, self.health, 20), 0, 10)

    def remove_health(self) -> None:
        self.health -= 1

    def draw(self, surface) -> None:
        surface.blit(self.image, self.rect)

class Stamina(pygame.sprite.Sprite):
    """ Stamina UI bar """
    def __init__(self, position, groups, stamina=50):
        super().__init__(groups)
        self.image = pygame.Surface((100, 50), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.stamina = 100
        self.position = position

    def update(self) -> None:
        pygame.draw.rect(self.image, '#6699ff', pygame.Rect(
            self.rect.x, self.rect.y, self.stamina, 20), 0, 10)

    def remove_stamina(self) -> None:
        self.stamina -= 1

    def draw(self, surface) -> None:
        surface.blit(self.image, self.rect)
