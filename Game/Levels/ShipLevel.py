from Game.Tile import Tile
from Game.Water import Water
from Game.Loaders.MapLoader import MapLoader


class ShipLevel:

    def create(self, engine):
        self.createOcean(engine)
        self.createShip(engine)

    def createOcean(self, engine):
        for y in range(-20, 40):
            for x in range(-24, 44):
                i = 0
                engine.addGameObject(Water(x * 16, y * 16, "Water"))


    def createShip(self, engine):
        mapLoader = MapLoader()
        mapData = mapLoader.load()

        textues = mapData["tiles"]
        sprites = {}
        path = "Mapa\\"
        for texture in textues:
            name = texture["name"]
            o = {}
            o["sprite"] =  engine.loadImage(path + name)
            o["name"]= name
            id = int(texture["id"])+1
            sprites[id] =o

        tilesIndexes = mapData["map"]
        height = mapData["height"]
        width = mapData["width"]
        offset = (-500, -500)
        for y in range(0, height):
            for x in range(0, width):
                spriteIndex = tilesIndexes[y * width + x]
                if spriteIndex == 0:
                    continue
                if spriteIndex not in sprites:
                    print("Sprite not found: ",spriteIndex)
                    continue

                spriteImage = sprites[spriteIndex]
                sprite = spriteImage["sprite"]
                name = spriteImage["name"]
                tile = None
                if "Barrier" in name:
                    tile = Tile(offset[0] + x * 16, offset[1] + y * 16, "wall", sprite=sprite,convert=False)
                else:
                    tile = Tile(offset[0] + x * 16, offset[1] + y * 16, name, sprite=sprite)
                engine.addGameObject(tile)
