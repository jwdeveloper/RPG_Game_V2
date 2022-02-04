from Engine.GameObject import GameObject
import math


class Quest(GameObject):
    owner = None
    isCompleted = False
    angle = 0

    def onEnable(self, engine):
        self.group = "quest"
        self.setImage(engine.loadImage("UI\\Quest"))

    def setOwner(self, gameObject):
        self.owner = gameObject

    def hasOwner(self):
        return self.owner != None

    def onTick(self, engine):

        if self.isCompleted:
            return

        if not self.hasOwner():
            return

        self.angle += 10
        self.angle %= 360
        offSet = math.sin(math.radians(self.angle))
        offSet *= 3

        x = self.owner.location.X()
        y = self.owner.location.Y() - self.location.height() - offSet
        self.location.set(x, y)
