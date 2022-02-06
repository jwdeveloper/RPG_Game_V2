from Engine.GameObject import GameObject
import math


class Quest(GameObject):
    owner = None
    isCompleted = False
    angle = 0
    isStarted = False
    player = None

    def onQuestCheck(self, engine):
        pass

    def onQuestStart(self, engine):
        pass

    def onQuestCompleted(self, engine):
        pass

    def begin(self):
        if self.isCompleted == True:
            return
        if self.isStarted == True:
            return

        self.onQuestStart(self.engine)

    def check(self):
        if self.isCompleted == True:
            return
        result = self.onQuestCheck(self.engine)
        if result:
            self.onQuestCompleted(self.engine)
            self.isCompleted = True

    def onEnable(self, engine):
        self.group = "quest"
        self.engine = engine
        self.camera = engine.findGameObject("camera")
        self.setImage(engine.loadImage("UI\\Quest"))

    def setOwner(self, gameObject):
        self.owner = gameObject
        self.player = gameObject.player

    def hasOwner(self):
        return self.owner != None

    def onTick(self, engine):

        if self.isStarted:
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
