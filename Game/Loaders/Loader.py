import os
from bs4 import BeautifulSoup as BS


class Loader:
    QUEST = "quest"
    ITEM = "item"
    SOUND = "sound"
    TEXTURE = "texture"
    NPC = "npc"

    def getFiles(self, path):
        basePath = 'Resources' + os.sep + 'GameObjects' + os.sep + path
        files = []
        for r, d, f in os.walk(basePath):
            for file in f:
                if file.endswith(".html"):
                    files.append(os.path.join(r, file))
        return files

    def getFileContent(self, path):
        with open(path) as file:
            return BS(file, 'html.parser')

    def copyAttributs(self, fromObj, toObj):
        for key in fromObj.attrs:
            toObj[key] = fromObj.attrs[key]

    def copyContent(self, fromObj, toObj):
        toObj["content"] = fromObj.contents

    def getTagContent(self, content, tagName):
        tag = content.find(tagName)
        result = {}
        if tag is None:
            return result
        result["content"] = ""
        self.copyAttributs(tag, result)
        for content in tag.contents:
            result["content"] += content
        return result

    def getContent(self, tag):
        result = ""
        for content in tag.contents:
            result += content
        return result

    def getTagGroup(self, content, groupName, childName):
        groupTag = content.find(groupName)
        result = []
        if groupTag is None:
            return result

        childsTag = groupTag.find_all(childName)
        for childTag in childsTag:
            child = {}
            self.copyAttributs(childTag, child)
            self.copyContent(childTag, child)
            result.append(child)
        return result

    def getTagStats(self, content):
        groupTag = content.find("stats")
        result = {}
        if groupTag is None:
            return result

        for content in groupTag.contents:
            lines = content.split("\n")
            for line in lines:
                line = line.replace(" ", "")
                if len(line) == 0:
                    continue
                stat = line.split(":")
                if len(stat) == 0:
                    continue
                result[stat[0]] = stat[1]
        return result

    def hasTag(self, file, tag):
        return file.find(tag) != None
