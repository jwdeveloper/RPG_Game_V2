from Engine.GameObject import GameObject
from Game.Entity import Entity
import random
import pygame
import math
from Game.Npc import Npc
from Game.Quests.Quest import Quest

class Pirate(Npc):

    quest = None

    def onEnable(self, engine):
        super().onEnable(engine)
        sprites = engine.loadImages("Postacie\\Alojzy")
        self.image = sprites[0]
        self.orignalImg = self.image
        self.sounds = engine.loadSounds("Pirat")
        self.soundQuest = engine.loadSound("Pirat\\Quest\\Zadanie_0.mp3")
        self.soundQuest2 = engine.loadSound("Pirat\\Quest\\CzyGotowe.mp3")
        self.location.set(30,30)

    def onTick(self, engine):
        super().onTick(engine)
        self.questAccept(engine.userInput,engine)

    def questAccept(self, input, engine):


        if input[pygame.K_e] and self.state == "talking":

            if self.quest != None:
                self.soundQuest2.play()
                return

            self.soundQuest.play()
            self.quest = Quest()
            self.quest.setOwner(self)
            engine.addGameObject(self.quest)


