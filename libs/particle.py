import pygame
from pygame.locals import *

import random
import math


class Particle(pygame.sprite.Sprite):
    """ White circle 'smoke' particles sort of like unity's particle system.
        These particles will appear when the player sprints.
    """
    def __init__(self, groups):
        super().__init__(groups)
