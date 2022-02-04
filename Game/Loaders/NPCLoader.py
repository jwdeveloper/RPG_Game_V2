import os
from Game.Loaders.Loader import Loader


class NPCLoader(Loader):

    def load(self):
        files = self.getFiles("NPC")
        result = []
        for file in files:
            content = self.readFile(file)
            result.append(content)

        return result

    def readFile(self, path):

        content = self.getFileContent(path)
        if not self.hasTag(content, self.NPC):
            return

        result = {}
        questTag = content.find(self.NPC)
        self.copyAttributs(questTag, result)
        result["stats"] = self.getTagStats(content)
        result["textures"] = self.getTagGroup(content, "textures", self.TEXTURE)
        result["sounds"] = self.getTagGroup(content, "sounds", self.SOUND)
        result["quests"] = self.getTagGroup(content, "quests", self.QUEST)
        result["items"] = self.getTagGroup(content, "items", self.ITEM)

        return result



