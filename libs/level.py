import os
import sys
import pygame

import pytmx

from .ui import *
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
        self.player = Group()

        # Position is static
        self.ui_bars = pygame.sprite.Group()

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

        self.health_bar = Health((10, 10), self.ui_bars)


        self.count_tiles = 0
        self.count_characters = 0
        self.count_enemies = 0


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
                            self.count_tiles += 1
                            # draw_loading(self.count_tiles, self.count_characters, self.count_enemies)
                            Tile(image=tile,
                                       position=(x * self.level_data.tilewidth, y * self.level_data.tileheight),
                                       groups=(self.tiles, self.all_sprites))
                        elif properties['player']:
                            self.count_characters += 1
                            self.player = Player(
                                          image=tile,
                                          position=(x * self.level_data.tilewidth, y * self.level_data.tileheight),
                                          groups=(self.player, self.all_sprites))
                        elif properties['enemy']:
                            self.count_enemies += 1
                            # draw_loading(self.count_tiles, self.count_characters, self.count_enemies)
                            Enemy(image=tile,
                                        position=(x * self.level_data.tilewidth, y * self.level_data.tileheight),
                                        groups=(self.enemies, self.all_sprites))

        self.target = self.player

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
            self.target.update()
            self.enemies.update()
            self.target.hitbox = self.all_sprites.target_hitbox
            print(self.target.hitbox)
            for sprite in self.enemies:
                if pygame.Rect.colliderect(sprite.rect, self.all_sprites.target_hitbox):
                    print("Player colliding with enemy")
                pygame.draw.rect(sprite.image, (255, 0, 0), sprite.rect, 3, 0)

            self.all_sprites.draw_ctx(self.screen, self.target)
            pygame.draw.circle(self.screen, (255, 0, 0), 
                    (self.mp[0]+1, self.mp[1]+1), 2)
            # Draw ui
            for actor in self.ui_bars:
                actor.update()
                actor.draw(self.screen)


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

