import math
import pygame
from pygame.locals import *
from .util import *
from .consts import *
from .ui import *


class Player(pygame.sprite.Sprite):
    """player"""
    def __init__(self, image, position, groups):
        super().__init__(groups)
        self.window = pygame.display.get_surface()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.position = pygame.math.Vector2(self.rect.x, self.rect.y)
        self.motion = False
        self.pressing = []
        self.acc = pygame.math.Vector2(0, 0)
        self.vel = pygame.math.Vector2(0, 0)
        self.hitbox = pygame.Rect(0, 0, 0, 0)
        self.colliding = False
        self.sprinting = False
        self.buffer = 0.5

    def recv_input(self):

        key = pygame.key.get_pressed()
        self.pressing = any((key[K_UP], key[K_DOWN], key[K_LEFT], key[K_RIGHT]))
        self.sprinting = (pygame.key.get_mods() & pygame.KMOD_SHIFT) and self.pressing

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
        
        if self.pressing:
            if self.vel.magnitude() > 0:
                self.vel = self.vel.normalize()
        else:
            if self.vel.magnitude() == 0:
                self.acc = pygame.math.Vector2(0, 0)

        if self.sprinting:
            self.buffer = 2
        else:
            self.buffer = 0.5

    def move(self):

        self.motion = self.vel.magnitude() > 0.3
        
        self.acc.x += self.vel.x * FRIC
        self.acc.y += self.vel.y * FRIC

        self.vel += self.acc
        self.position += self.vel + self.buffer * self.acc

        self.rect.centerx = self.position.x // 2
        self.rect.centery = self.position.y // 2


    def update(self):
        self.recv_input()
        self.move()
