import pygame
from Engine.Location import Location


class GameObject(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = None
        self.name = "GameObject"
        self.group = "default"
        self.rect = pygame.Rect((0, 0), (0, 0))
        self.location = Location(self.rect)
        self.image = None

        self.isActive = True
        self.shouldDestroy = False

    # Methods that can be overridden

    def onEnable(self, engine):
        pass

    def onTick(self, engine):
        pass

    def onCollision(self, engine, gameObject):
        pass

    # =====================================

    def isActive(self):
        if self.image or self.rect is None:
            return False

        return self.isActive

    def setImage(self, image):
        self.image = image
        self.surf = image
        self.rect = image.get_rect()
        self.location = Location(self.rect)
        self.mask = pygame.mask.from_surface(self.image)

    def getColliderBox(self):
        if self.enableCollision is False or self.hasTexture() is False:
            return None
        self.rect.center = (self.location.x, self.location.y)
        return self.rect

    def destroy(self):
        self.shouldDestroy = True
