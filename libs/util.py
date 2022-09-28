import pygame
from .spritesheet import spritesheet as ss
from .sprite_strip_anim import SpriteStripAnim as ssa
from .consts import WHITE, font
from pytmx import load_pygame, TiledTileLayer, TiledMap

def load_tilemap(map_: str) -> object:
    tmx_data   = TiledMap(map_)
    tmx_width  = tmx_data.width  * tmx_data.tilewidth
    tmx_height = tmx_data.height * tmx_data.tileheight
    tmx_image  = tilemap.get_tile_image_by_gid

    return tmx_data

def load_image(image, colorkey: tuple, root):
    spritesheet =  ss()

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
