from Engine.GameObject import GameObject


class Tile(GameObject):

    def __init__(self, x, y, group, convert=True):
        super().__init__()
        self.startGroup = group
        self.startX = x
        self.startY = y
        self.convert = convert

    def onEnable(self, engine):
        self.group = self.startGroup
        if self.convert:
            self.setImage(engine.loadImage("Mapa\\" + self.startGroup).convert())
        else:
            self.setImage(engine.loadImage("Mapa\\" + self.startGroup))

        self.location.set(self.startX, self.startY)
