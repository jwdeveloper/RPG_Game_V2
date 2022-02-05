from Engine.GameObject import GameObject


class Tile(GameObject):

    def __init__(self, x, y, group, convert=True, sprite=None):
        super().__init__()
        self.group = group
        self.startX = x
        self.startY = y
        self.convert = convert
        self.sprite = sprite

    def onEnable(self, engine):

        if self.sprite == None:
            self.sprite = engine.loadImage("Mapa\\" + self.group)

        if self.convert:
            self.setImage(self.sprite.convert())
        else:
            self.setImage(self.sprite)

        self.location.set(self.startX, self.startY)
