import pygame.sprite
import math
import pygame


class GameGroup(pygame.sprite.Group):
    renderIndex = 0
    disableRender = False
    gameObjects = []
    renderDistance = 300

    def doTick(self, engine):
        toDestroy = []

        self.gameObjects = sorted(self.sprites(), key=lambda sprite: sprite.rect.centery)
        for sprite in self.gameObjects:
            if sprite.shouldDestroy:
                toDestroy.append(sprite)
                continue

            sprite.onTick(engine)

        for sprite in toDestroy:
            self.remove(sprite)

    def draw(self, surface, camera):

        if self.disableRender:
            return

        half_width = surface.get_size()[0] // 2
        half_height = surface.get_size()[1] // 2
        for sprite in self.gameObjects:
            if sprite.image is None:
                continue
            distance = self.distance(sprite.location.X(), sprite.location.Y(), camera.x, camera.y)
            if distance > self.renderDistance:
                continue

            x = sprite.location.X() - camera.x + half_width - sprite.location.width() // 2
            y = sprite.location.Y() - camera.y + half_height - sprite.location.height() // 2
            surface.blit(sprite.image, (x, y))

    def distance(self, x1, y1, x2, y2):
        return math.hypot(x1 - x2, y1 - y2)
