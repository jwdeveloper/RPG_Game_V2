from Engine.GameObject import GameObject
import pygame


class Entity(GameObject):
    rotate = 1
    speed = 3
    stats = {}
    health_capacity = 100
    current_health = 0

    def onEnable(self, engine):
        self.right = None
        self.left = None
        self.stats['health'] = 50
        self.stats['energy'] = 50


    def turnLeft(self):
        if self.left is None:
            self.left = pygame.transform.flip(self.image, True, False)
        self.image = self.left

    def turnRight(self):
        if self.right is None:
            self.right = pygame.transform.flip(self.image, False, False)
        self.image = self.right

    def onTick(self, engine):
        engine.checkCollision(self, "wall")

    def onCollision(self, engine, gameObject):

        if gameObject.group == "wall":
            x = self.location.lastX
            y = self.location.lastY
            self.location.set(x, y)
        else:
          d = self.location.direction(gameObject.location)
          self.location.add(d[0], d[1])
