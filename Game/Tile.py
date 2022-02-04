from Engine.GameObject import GameObject


class Tile(GameObject):

    def __init__(self, x, y,group):
        super().__init__()
        self.startGroup = group
        self.startX = x
        self.startY = y

    def onEnable(self, engine):
        self.group = self.startGroup
        self.setImage(engine.loadImage("Mapa\\"+self.startGroup).convert())
        self.location.set(self.startX, self.startY)


