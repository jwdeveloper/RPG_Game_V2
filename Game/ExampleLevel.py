from Game.Tile import Tile
from Game.Water import Water


class ExampleLevel:

    def create(self, engine):
        self.createOcean(engine)
        self.createRoom(engine)
        self.topBarrier(engine)

    def createOcean(self, engine):
        for y in range(-20, 40):
            for x in range(-40, 40):
                i = 0
                engine.addGameObject(Water(x * 16, y * 16, "Water"))

    def topBarrier(self, engine):
        for x in range(0, 20):
            tile = Tile(x * 16, 0, "Barrier",False)
            tile.name = f"Barrier {x} {0}"
            engine.addGameObject(tile)

    def createRoom(self, engine):
        for y in range(1, 20):
            for x in range(0, 20):
                if (y == 0 or x == 0) or ( x == 19):
                    tile = Tile(x * 16, y * 16, "Wood_Barrier_Top")
                    tile.name = f"Wall {x} {y}"
                    engine.addGameObject(tile)
                    continue
                if y == 19:
                    tile = Tile(x * 16, y * 16, "Wood_Barrier")
                    tile.name = f"Wall {x} {y}"
                    engine.addGameObject(tile)
                    continue
                else:
                    engine.addGameObject(Tile(x * 16, y * 16, "Wood"))
