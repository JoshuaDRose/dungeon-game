import os
import sys
import pygame

import pytmx

from .util import *
from .consts import *
from .tile import Tile
from .player import Player
from .enemy import Enemy

ctx = {}
ctx['game'], ctx['pause'] = 1, 0

class Level:
    def __init__(self, tmx_map):
        self.level_data = pytmx.load_pygame(tmx_map, pixelalpha=True)

        self.width = self.level_data.tilewidth * self.level_data.width
        self.height = self.level_data.tileheight * self.level_data.height

        self.buttons = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.tiles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self.screen = pygame.display.get_surface()
        self.map_data = pytmx.TiledMap(tmx_map)
        self.tilemap = os.path.join('./art/Tilemap/tilemap.png')

        for layer in self.map_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = self.level_data.get_tile_image_by_gid(gid)
                    properties = self.level_data.get_tile_properties_by_gid(gid)
                    if tile:
                        if properties['tile']:
                            Tile(
                                    image=tile,
                                    position=(x * self.level_data.tilewidth, y * self.level_data.tileheight),
                                    groups=(self.tiles, self.all_sprites)
                                )
                        elif properties['player']:
                            Player(
                                    image=tile,
                                    position=(x * self.level_data.tilewidth, y * self.level_data.tileheight),
                                    groups=(self.tiles, self.all_sprites)
                                )
                        elif properties['enemy']:
                            Enemy(
                                    image=tile,
                                    position=(x * self.level_data.tilewidth, y * self.level_data.tileheight),
                                    groups=(self.tiles, self.all_sprites)
                                )

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # x2 buttons: "Are you sure you want to quit?" [y] [n] ...
                if ctx['game']:
                    pygame.quit()
                    sys.exit()
                else:
                    pygame.quit()
                    sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.quit()
                    sys.exit()

            if ctx['game']:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        # inversion minimizes syntax logic
                        ctx['pause'] = not ctx['pause']

        if ctx['game']:
            self.all_sprites.draw(self.screen)
