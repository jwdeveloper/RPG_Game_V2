import os
from Game.Loaders.Loader import Loader
from bs4 import BeautifulSoup as BS


class QuestLoader(Loader):

    def load(self):
        files = self.getFiles("Quests")
        result = []
        for file in files:
            content = self.readFile(file)
            result.append(content)

        return result

    def readFile(self, path):

        content = self.getFileContent(path)
        if not self.hasTag(content, self.QUEST):
            return

        result = {}
        questTag = content.find(self.QUEST)
        self.copyAttributs(questTag, result)
        result["reward"] = self.getRewards(content)
        result["dialogs"] = self.getDialogs(content)

        return result

    def getRewards(self, content):
        rewardTag = content.find("reward")
        if rewardTag is None:
            return None

        reward = []
        itemsTag = rewardTag.find_all(self.ITEM)
        for itemTag in itemsTag:
            item = {}
            self.copyAttributs(itemTag, item)
            self.copyContent(itemTag, item)
            item["type"] = "item"
            reward.append(item)
        return reward

    def getDialogs(self, content):
        dialgosTag = content.findAll("dialog")
        dialogs = []
        for dialogTag in dialgosTag:
            dialog = {}
            dialog["messages"] = []
            self.copyAttributs(dialogTag, dialog)
            for messageTag in dialogTag.findAll("message"):
                message = {}
                self.copyAttributs(messageTag, message)
                message["text"] = []
                for textTag in messageTag.findAll("text"):
                    text = self.getContent(textTag)
                    message["text"].append(text)

                message["options"] = []
                for optionTag in messageTag.findAll("option"):
                    option = self.getContent(optionTag)
                    message["options"].append(option)
                dialog["messages"].append(message)
            dialogs.append(dialog)
        return dialogs
