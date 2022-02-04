import pygame
from Game.Npc import Npc
from Game.Quests.Quest import Quest

class Sapling(Npc):

    quest = None

    def onEnable(self, engine):
        super().onEnable(engine)
        sprites = engine.loadImages("Postacie\\Norbert")
        self.image = sprites[0]
        self.orignalImg = self.image
        self.sounds = engine.loadSounds("Pirat")
        self.soundQuest = engine.loadSound("Pirat\\Quest\\Zadanie_0.mp3")
        self.soundQuest2 = engine.loadSound("Pirat\\Quest\\CzyGotowe.mp3")
        self.location.set(30,30)
        self.camera = engine.findGameObject("camera")

    def onTick(self, engine):
       self.location.set(200,-100)




