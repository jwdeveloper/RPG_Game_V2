from Engine.GameObject import GameObject
import pygame
from Game.Entity import Entity
from Game.UI.PlayerUI import PlayerUI
from Engine import Math
import pygame_gui


class Player(Entity):
    def setUser(self, user):
        self.user = user

    def onEnable(self, engine):
        super().onEnable(engine)
        self.setImage(engine.loadImage("Postacie\\Klasy\\" + self.user.character))
        self.ui = PlayerUI()
        self.group = "player"
        self.name = "player"
        self.stats["exp"] = 20
        self.location.add(50, 50)
        self.camera = engine.findGameObject("camera")
        self.camera.setTarget(self)

    def onTick(self, engine):
        engine.checkCollision(self, "npc")
        self.controlEntity(engine.userInput, engine)
        super().onTick(engine)

    def onCollision(self, engine, gameObject):
        super().onCollision(engine, gameObject)
        if gameObject.group == "npc":
            self.npcInteract(engine, gameObject)

    def controlEntity(self, input, engine):

        if input[pygame.K_q]:
            engine.setZoom(engine.zoom_factor + 100)

        if input[pygame.K_s]:
            return self.location.add(0, 1 * self.speed)
        if input[pygame.K_w]:
            return self.location.add(0, -1 * self.speed)
        if input[pygame.K_a]:
            self.turnLeft()
            return self.location.add(-1 * self.speed, 0)
        if input[pygame.K_d]:
            self.turnRight()
            return self.location.add(1 * self.speed, 0)

    def npcInteract(self, engine, npc):

        if engine.isKeyUp(pygame.K_e):
            npc.checkQuest()
