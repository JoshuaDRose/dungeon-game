import pygame

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()

        self.split_width = self.screen.get_width() // 2
        self.split_height = self.screen.get_height() // 2

        self.offset = pygame.math.Vector2()

        self.scale = 3

        self.surface_size = (500, 500)
        self.surface = pygame.Surface(self.surface_size, pygame.SRCALPHA)
        self.rect = self.surface.get_rect(center=(self.split_width, self.split_height))
        self.movement = pygame.math.Vector2(self.surface_size)
        self.inner_offset = pygame.math.Vector2()
        self.inner_offset.x = self.surface_size[0] // 2 - self.split_width
        self.inner_offset.y = self.surface_size[1] // 2 - self.split_height
        

    def target_center(self, sprite: pygame.sprite.Sprite):
        self.offset.x = sprite.rect.centerx - self.split_width
        self.offset.y = sprite.rect.centery - self.split_height

    def draw_ctx(self, surface, target=None):

        self.surface.fill('#e3a56d')

        if target:
            self.target_center(target)

        try:
            for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
                offset_position = sprite.rect.topleft - self.offset
                self.surface.blit(sprite.image, offset_position)
        finally:
            offset_position = target.rect.topleft - self.offset + self.inner_offset
            self.surface.blit(target.image, offset_position)

        scaled_surf = pygame.transform.scale(self.surface, self.movement * self.scale)
        scaled_rect = scaled_surf.get_rect(center=(self.split_width, self.split_height))

        surface.blit(scaled_surf, scaled_rect)

