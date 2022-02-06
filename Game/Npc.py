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

    def onEnable(self, engine):
        super().onEnable(engine)
        self.group = "Npc"
        self.setImage(engine.loadImage("Postacie\\Pirate\\Pirate"))
        self.orignalImg = self.image
        self.location.add(200, 100)
        self.player = engine.findGameObject("player")
        self.sounds = engine.loadSounds("Kapitan")
        self.currenctSound = None

    def onTick(self, engine):
        super().onTick(engine)
        engine.checkCollision(self, "player")
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

    angle = 0
    startTalking = False

    def talking(self, engine):
        if self.startTalking == False:
            index = random.randint(0, len(self.sounds) - 1)
            self.currenctSound = self.sounds[index]
            self.currenctSound.play()
            self.startTalking = True

        self.angle += 10
        self.angle %= 360
        v = math.sin(math.radians(self.angle))
        v *= 10
        v = abs(v)
        self.image = pygame.transform.scale(self.orignalImg, (16, 16 + v))
        distance = self.location.distance(self.player.location)

        c = self.smoothAudio(distance)
        self.currenctSound.volume = 10

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
