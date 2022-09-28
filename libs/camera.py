import pygame

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()

        self.split_width = self.screen.get_width() // 2
        self.split_height = self.screen.get_height() // 2

        # Camera offset
        self.offset = pygame.math.Vector2(300, 100)


    def target_center(self, sprite: pygame.sprite.Sprite):
        self.offset.x = sprite.rect.centerx - self.split_width
        self.offset.y = sprite.rect.centery - self.split_height

    def draw_ctx(self, surface: pygame.Surface, target=None):

        if target:
            self.target_center(target)

        try:
            for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
                offset_position = sprite.rect.topleft - self.offset
                surface.blit(sprite.image, offset_position)
        finally:
            offset_position = target.rect.topleft - self.offset
            surface.blit(target.image, offset_position)
