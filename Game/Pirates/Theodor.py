import pygame
from Game.Npc import Npc
from Game.Quests.Quest import Quest

class Theodor(Npc):

    quest = None

    def onEnable(self, engine):
        super().onEnable(engine)
        sprites = engine.loadImages("Postacie\\Pirate")
        self.image = sprites[0]
        self.orignalImg = self.image
        self.sounds = engine.loadSounds("Pirat3")
        self.location.set(50,70)
        self.camera = engine.findGameObject("camera")





