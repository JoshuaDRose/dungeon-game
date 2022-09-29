import pygame
from .consts import font as ff
from .consts import center_surface

class Button(pygame.sprite.Sprite):
    def __init__(self, string, color, pos, groups, center=(0, 0)):
        super().__init__(groups)
        self.name = string
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
        
        self.border = pygame.Surface((
                self.rect.width + 20,
                self.rect.height + 10),
                pygame.SRCALPHA
        )

        self.border.fill((0, 0, 0))
        self.border.set_alpha(125)
        self.alpha = 125
        pygame.draw.rect(self.border, (255, 255, 255, 255), self.border.get_rect(), 3)
        self.border.blit(self.image, (
            abs(self.rect.width // 2 - self.border.get_width() // 2),
            abs(self.rect.height // 2 - self.border.get_height() // 2))
        )
        self.image = self.border

        self.hover = False

    def update(self):
        if self.hover:
            if self.alpha < 255:
                self.alpha += 10
                self.border.set_alpha(self.alpha)
            else:
                self.alpha = 255
        else:
            if self.alpha > 125:
                self.alpha -= 10
            else:
                self.alpha = 125
        self.image.set_alpha(self.alpha)

    def draw(self, surface) -> None:
        surface.blit(self.image, self.rect)
