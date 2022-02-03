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
        self.setImage(engine.loadImage("Paladyn"))
        self.orignalImg = self.image
        self.location.add(200, 100)
        self.player = engine.findGameObject("player")

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

    def talking(self, engine):

        self.angle += 10
        self.angle %= 360
        v = math.sin(math.radians(self.angle))
        v *= 10
        v = abs(v)
        self.image = pygame.transform.scale(self.orignalImg, (16, 16 + v))
        distance = self.location.distance(self.player.location)
        if distance > 3 * 16:
            self.state = "walking"
            return

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
