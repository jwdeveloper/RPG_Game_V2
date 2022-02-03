from Engine.GameObject import GameObject


class Tile(GameObject):

    def __init__(self, x, y):
        super().__init__()
        self.group = "Walls"
        self.startX = x
        self.startY = y

    def onEnable(self, engine):
        self.group = "wall"
        self.setImage(engine.loadImage("Wall"))
        self.location.set(self.startX, self.startY)

    def onCollision(self, engine, gameObject): pass
        #engine.log(f"Tile collide with {gameObject}")
