import pygame

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()

        self.split_width = self.screen.get_width() // 2
        self.split_height = self.screen.get_height() // 2

        self.offset = pygame.math.Vector2()

        # SCALE IS 3 -- DO NOT CHANGE
        self.default_scale = 3
        self.scale = 2 # decreases in sine when sprinting

        self.surface_size = (500, 500)
        self.surface = pygame.Surface(self.surface_size, pygame.SRCALPHA)
        self.rect = self.surface.get_rect(center=(self.split_width, self.split_height))
        self.movement = pygame.math.Vector2(self.surface_size)
        self.inner_offset = pygame.math.Vector2()
        self.inner_offset.x = self.surface_size[0] // 2 - self.split_width
        self.inner_offset.y = self.surface_size[1] // 2 - self.split_height
        
        self.target_hitbox = pygame.Rect(0, 0, 0, 0)

        self.zoom_out = 0
        self.player = 0

    def zoom_monitor(self):
        if self.zoom_out:
            # if further away than allowed
            if self.scale < 2.7:
                self.scale = 2.7
            # else do normal zoom out
            if self.scale > 2.7:
                self.scale -= .1
        else:
            # if closer than allowed
            if self.scale > 3:
                # set to default
                self.scale = 3
            # else do normal zoom in
            if self.scale < 3:
                self.scale += .1

    def target_center(self, sprite: pygame.sprite.Sprite):
        self.offset.x = sprite.rect.centerx - self.split_width
        self.offset.y = sprite.rect.centery - self.split_height

    def get_player(self):
        print("camera.cameraGroup.get_player > retrieving player from index")
        for sprite in sorted(self.sprites(),key=lambda sprite: sprite.rect):
            if '__player__' in sprite.__dir__():
                print("Done")
                return sprite

    def draw_ctx(self, surface, target=None):


        if not self.player:
            self.player = self.get_player()
        if target:
            self.target_center(target)

        try:
            for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect):
                offset_position = sprite.rect.topleft - self.offset
                self.surface.blit(sprite.image, offset_position)

        finally:
            offset_position = target.rect.topleft - self.offset + self.inner_offset
            self.surface.blit(target.image,
                    (offset_position[0], offset_position[1]))

            self.target_hitbox = pygame.Rect(
                target.rect.topleft[0] - self.offset[0] - 230,
                target.rect.topleft[1] - self.offset[1] - 70,
                target.rect.width,
                target.rect.height)

            # pygame.draw.rect(self.surface, (255,0,0), self.target_hitbox, 3, 0)
        # NOTE do all player collision in here

        scaled_surf = pygame.transform.scale(self.surface, self.movement * self.scale)
        scaled_rect = scaled_surf.get_rect(center=(self.split_width, self.split_height))

        surface.blit(scaled_surf, scaled_rect)

