from Game.Tile import Tile
from Game.Water import Water

class ExampleLevel:

    def create(self, engine):
        self.createOcean(engine)
        self.createRoom(engine)

    def createOcean(self, engine):
        for y in range(-20, 40):
            for x in range(-40, 40):
                i=0
                engine.addGameObject(Water(x * 16, y * 16, "Water"))

    def createRoom(self, engine):
        for y in range(0, 20):
            for x in range(0, 20):
                if (y == 0 or x == 0) or (y == 19 or x == 19):
                    tile = Tile(x * 16, y * 16, "Wall")
                    tile.name = f"Wall {x} {y}"
                    engine.addGameObject(tile)
                else:
                    engine.addGameObject(Tile(x * 16, y * 16, "Wood"))
