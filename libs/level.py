import os
import sys
import pygame

import pytmx

from .util import *
from .consts import *
from .tile import Tile
from .player import Player
from .enemy import Enemy
from .button import Button
from .camera import CameraGroup as Group

ctx = {'game': 0, 'pause': 0, 'menu': 1, 'settings': 0}


class Level:
    def __init__(self, tmx_map):
        self.level_data = pytmx.load_pygame(tmx_map, pixelalpha=True)

        self.width = self.level_data.tilewidth * self.level_data.width
        self.height = self.level_data.tileheight * self.level_data.height

        self.buttons = Group()
        self.coins = Group()
        self.tiles = Group()
        self.enemies = Group()
        self.all_sprites = Group()

        self.screen = pygame.display.get_surface()

        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()

        self.map_data = pytmx.TiledMap(tmx_map)
        self.tilemap = os.path.join('./art/Tilemap/tilemap.png')

        self.title_map_location = '/home/qwerty/projects/python/dungeon-game/art/Tiled/titleMap.tmx'

        self.title_screen = pytmx.load_pygame(
            os.path.join(self.title_map_location),
            pixelalpha=True
        )
        self.title_tiles = pygame.sprite.Group()

        self.mp = pygame.mouse.get_pos()
        self.mclick = False

        ### TEST BUTTON ###

        self.play = Button(
                "Play",
                (255, 255, 255),
                (0, 200),
                groups=self.buttons,
                center=(1, 0)
        )


        self.settings = Button(
                "Settings",
                (255, 255, 255),
                (0, 300),
                groups=self.buttons,
                center=(1, 0)
        )

        self.quit = Button(
                "Quit",
                (255, 255, 255),
                (0, 400),
                groups=self.buttons,
                center=(1, 0)
        )
        
        for layer in self.title_screen:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = self.title_screen.get_tile_image_by_gid(gid)
                    if tile:
                        tile = pygame.transform.scale(tile, (64, 64))
                        Tile(image=tile,
                                position=(x * self.title_screen.tilewidth, y * self.title_screen.tilewidth),
                                groups=(self.title_tiles))

        for layer in self.map_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = self.level_data.get_tile_image_by_gid(gid)
                    properties = self.level_data.get_tile_properties_by_gid(gid)
                    if tile:
                        if properties['tile']:
                            Tile(image=tile,
                                       position=(x * self.level_data.tilewidth, y * self.level_data.tileheight),
                                       groups=(self.tiles, self.all_sprites))
                        if properties['player']:
                            self.player = Player(
                                          image=tile,
                                          position=(x * self.level_data.tilewidth, y * self.level_data.tileheight),
                                          groups=(self.all_sprites))
                        if properties['enemy']:
                            Enemy(image=tile,
                                        position=(x * self.level_data.tilewidth, y * self.level_data.tileheight),
                                        groups=(self.tiles, self.all_sprites))

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

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mclick = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.mclick = False

            if event.type == pygame.MOUSEMOTION:
                self.mp = pygame.mouse.get_pos()

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
            self.player.update()
            self.all_sprites.draw_ctx(self.screen, target=self.player)

        elif ctx['menu']:
            self.title_tiles.draw(self.screen)
            for button in self.buttons:
                button.update()
                if pygame.Rect.collidepoint(button.rect, self.mp):
                    button.hover = True
                    if self.mclick:
                        if button.name.lower() == 'play':
                            ctx['game'] = 1
                            ctx['menu'] = 0
                        elif button.name.lower() == 'quit':
                            pygame.quit()
                            sys.exit(0)
                else:
                    button.hover = False
                button.draw(self.screen)

