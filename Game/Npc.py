from Engine.GameObject import GameObject
from Game.Entity import Entity
import random
import pygame
import math


class Npc(Entity):
    directionX = 0
    directionY = 0
    tickDelay = 3000
    speed = 1
    state = "walking"
    rotated = False
    orignalImg = None
    player = None
    angle = 0
    startTalking = False

    def onEnable(self, engine):
        super().onEnable(engine)
        self.group = "npc"
        self.setImage(engine.loadImage("Postacie\\Pirate\\Pirate"))
        self.orignalImg = self.image
        self.location.add(200, 100)
        self.player = engine.findGameObject("player")
        self.sounds = engine.loadSounds("Kapitan")
        self.currenctSound = None
        self.quest = None
        self.engine = engine

    def onTick(self, engine):
        super().onTick(engine)

        if self.state == "walking":
            self.walking(engine)
        if self.state == "talking":
            self.talking(engine)

    def onCollision(self, engine, gameObject):
        super().onCollision(engine, gameObject)
        if gameObject.group == "player":
            self.state = "talking"
        else:
            self.state = "walking"

    def setQuest(self, quest):
        self.quest = quest
        self.engine.addGameObject(quest)

    def talking(self, engine):
        if self.startTalking == False:
            index = random.randint(0, len(self.sounds) - 1)
            self.currenctSound = self.sounds[index]
            self.playSound(self.currenctSound)
            self.startTalking = True

        self.angle += 10
        self.angle %= 360
        v = math.sin(math.radians(self.angle))
        v *= 10
        v = abs(v)
        self.image = pygame.transform.scale(self.orignalImg, (16, 16 + v))
        distance = self.location.distance(self.player.location)

        self.currenctSound.volume = self.smoothAudio(distance)

        if distance > 5 * 16:
            self.state = "walking"
            self.startTalking = False
            return

    def smoothAudio(self, x):
        if x == 0:
            return 50
        v = abs(-math.log(x * math.e) * 0.004 * x * x + 100)
        if v > 100:
            v = 0
        return v

    def walking(self, engine):
        if engine.currentTick > self.tickDelay:
            ticks = random.randint(0, 2) * 1000
            self.tickDelay = engine.currentTick + ticks
            self.directionX = random.randint(-1, 1)
            self.directionY = random.randint(-1, 1)
            if self.directionX > 0:
                self.turnRight()
            else:
                self.turnLeft()

        self.location.add(self.speed * self.directionX, self.speed * self.directionY)

    def checkQuest(self):
        if self.quest is None or self.quest.isCompleted:
            return
        if self.quest.isStarted is False:
            self.quest.begin()
        else:
            self.quest.check()
