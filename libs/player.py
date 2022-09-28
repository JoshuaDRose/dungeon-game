import pygame
from pygame.locals import *
from .util import *
from .consts import *

class Player(pygame.sprite.Sprite):
    def __init__(self, image, position, groups):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.position = pygame.math.Vector2(self.rect.x, self.rect.y)
        self.direction = pygame.math.Vector2()
        self.vel = 5

    def recv_input(self):
        key = pygame.key.get_pressed()

        if key[K_UP]:
            self.direction.y = -1
        elif key[K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        if key[K_LEFT]:
            self.direction.x = -1
        elif key[K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def update(self):
        self.recv_input()
        self.rect.center += self.direction * self.vel
