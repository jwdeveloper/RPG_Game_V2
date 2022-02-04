from Engine.GameObject import GameObject
import math

class Item(GameObject):
    questOwner = None
    isCompleted = False

    def onEnable(self, engine):
        self.group = "items"
        self.setImage(engine.loadImage("UI\\Quest"))
        self.angle = 0

    def setOwner(self, gameObject):
        self.questOwner = gameObject

    def onTick(self, engine):

        if self.isCompleted:
            return

        if self.questOwner == None:
            return

        self.angle += 10
        self.angle %= 360
        offSet = math.sin(math.radians(self.angle))
        offSet *=3

        x = self.questOwner.location.X()
        y = self.questOwner.location.Y() - self.location.height()-offSet
        self.location.set(x, y)
