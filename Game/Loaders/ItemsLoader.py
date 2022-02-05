import os
from Game.Loaders.Loader import Loader


class ItemsLoader(Loader):

    def load(self):
        files = self.getFiles("Items")
        result = []
        for file in files:
            content = self.readFile(file)
            result.append(content)

        return result

    def readFile(self, path):

        content = self.getFileContent(path)
        if not self.hasTag(content, self.ITEM):
            return

        result = {}
        questTag = content.find(self.ITEM)
        self.copyAttributs(questTag, result)
        result["stats"] = self.getTagStats(content)
        result["name"] = self.getTagContent(content, "name")
        result["description"] = self.getTagContent(content, "description")
        result["textures"] = self.getTagGroup(content, "textures", self.TEXTURE)
        result["sounds"] = self.getTagGroup(content, "sounds", self.SOUND)
        return result
