import pygame
from .consts import font as ff
from .consts import center_surface

class Button(pygame.sprite.Sprite):
    def __init__(self, string, color, pos, groups=None, center=(0, 0)):
        if groups:
            super().__init__(groups)
        else:
            super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.image = ff.render(string, True, color)
        self.rect = self.image.get_rect()
        if center[0]:
            self.rect.x = center_surface(
                self.display_surface.get_rect(), self.image.get_rect(),
                c=(1, 0)
            )
        if center[1]:
            self.rect.y = center_surface(
                self.display_surface.get_rect(), self.image.get_rect(),
                c=(0, 1))
        if not center[0]:
            self.rect.x = pos[0]
        if not center[1]:
            self.rect.y = pos[1]



