import pygame
from .consts import *


class Health(pygame.sprite.Sprite):
    """ UI health bar """
    def __init__(self, position, groups, health=100):
        super().__init__(groups)
        self.image = pygame.Surface((150, 30), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.health = health
        self.position = position

    def update(self) -> None:
        pygame.draw.rect(self.image, (200, 45, 10), pygame.Rect(
            self.rect.x, self.rect.y, self.health, 30), 0, 10)

    def remove_health(self, amount: int) -> None:
        amount = -abs(amount)
        self.health -= 1

    def draw(self, surface) -> None:
        surface.blit(self.image, self.rect)
