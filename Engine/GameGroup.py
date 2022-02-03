import pygame.sprite


class GameGroup(pygame.sprite.Group):
    renderIndex = 0
    disableRender = False

    def draw(self, surface, camera):

        if self.disableRender:
            return

        half_width = surface.get_size()[0] // 2
        half_height = surface.get_size()[1] // 2
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            if sprite.image is None:
                continue
            x = sprite.location.X() - camera.x+half_width-sprite.location.width()//2
            y = sprite.location.Y() - camera.y+half_height-sprite.location.height()//2
            surface.blit(sprite.image, (x,y))
