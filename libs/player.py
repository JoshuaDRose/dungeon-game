import math
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
        self.motion = False
        self.acc = pygame.math.Vector2(0, 0)
        self.vel = pygame.math.Vector2(0, 0)

    def recv_input(self):
        key = pygame.key.get_pressed()

        if key[K_UP]:
            self.acc.y = -ACC
        elif key[K_DOWN]:
            self.acc.y = ACC
        else:
            self.acc.y = 0
        if key[K_LEFT]:
            self.acc.x = -ACC
        elif key[K_RIGHT]:
            self.acc.x = ACC
        else:
            self.acc.x = 0

    def move(self):

        self.motion = self.vel.magnitude() > 0.3
        self.acc.x += self.vel.x * FRIC
        self.acc.y += self.vel.y * FRIC

        self.vel += self.acc
        self.position += self.vel + 0.5 * self.acc

        self.rect.centerx = self.position.x // 2
        self.rect.centery = self.position.y // 2


    def update(self):
        self.recv_input()
        self.move()
