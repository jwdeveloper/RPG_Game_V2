from Engine.GameObject import GameObject
import math

class Item(GameObject):


    stats = []
    owner = None

    def onEnable(self, engine):
        self.group = "items"

    def setOwner(self, gameObject):
        self.owner = gameObject

    def onTick(self, engine):

        if not self.hasOwner():
            return

    def hasOwner(self):
        return self.owner != None