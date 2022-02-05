import json
from Game.Loaders.Loader import Loader
import os


class MapLoader(Loader):

    path = 'Resources' + os.sep + 'GameObjects' +os.sep +"Maps"+ os.sep +"Statek"+ os.sep


    def load(self):
        ship = self.loadJson(self.path + "Statek.json")
        textures = self.loadJson(self.path + "Statek_Textures.json")
        res = {}
        res["height"] = ship["height"]
        res["width"] = ship["width"]
        res["map"] = ship["layers"][0]["data"]
        res["tiles"] = []
        for texture in textures["tiles"]:
            tile = {}
            tile["id"] = texture["id"]

            path = texture["image"]
            start = path.rfind("/")+1
            end = path.rfind(".")
            tile["name"] = path[start:end]
            res["tiles"].append(tile)


        return res


    def loadJson(self, path):

        try:
            with open(path, "r+") as file:
                content = file.read()

                return json.loads(content)

        except Exception as error:
            print("File loadin error", error)

        return None
