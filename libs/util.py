import pygame
from .consts import WHITE, font

def draw_text(text, pos, center=False):
    # global font
    return font.render(
            text=text,
            antialias=True,
            color=WHITE,
            background=None)


def center_text(text: pygame.Surface) -> pygame.Rect:
    rect = text.get_rect()
    screen = pygame.display.get_surface()
    return (screen.width // 2 - rect.width // 2,
           screen.height // 2 - rect.height // 2)
