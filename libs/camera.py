import pygame

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()

        # Camera offset
        self.offset = pygame.math.Vector2(300, 100)

    def draw_ctx(self, surface):
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_position = sprite.rect.topleft + self.offset
            surface.blit(sprite.image, offset_position)
