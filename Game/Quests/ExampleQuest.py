from Engine.GameObject import GameObject
from Game.Quests import Quest

class ExampleQuest(Quest):

    def onQuestStart(self, engine):
        self.sound_quest_start = self.owner.questSounds[0]
        self.sound_is_ready = self.owner.questSounds[1]
        self.sound_get_lost = self.owner.questSounds[2]

        self.owner.playSound(self.sound_quest_start)

    pass

    def onQuestCheck(self, engine):
        self.owner.playSound(self.sound_get_lost)
        pass

    def onQuestCompleted(self, engine):
        self.owner.playSound(self.sound_is_ready)
        pass
