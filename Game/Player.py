from Engine.GameObject import GameObject
import pygame
from Game.Entity import Entity
from Game.UI.PlayerUI import PlayerUI
from Engine import Math
import pygame_gui


class Player(Entity):
    def setUser(self,user):
        self.user=user

    def onEnable(self, engine):
        super().onEnable(engine)
        self.setImage(engine.loadImage("Postacie\\Klasy\\"+self.user.character))
        self.ui = PlayerUI()
        self.group = "player"
        self.name = "player"
        self.stats["exp"] = 20
        self.location.add(50, 50)
        self.camera = engine.findGameObject("camera")
        self.camera.setTarget(self)

    def onTick(self, engine):

        self.controlEntity(engine.userInput)
        self.zoomControl(engine.userInput, engine)
        super().onTick(engine)
        self.rozmawiaj(engine.userInput,engine)
        self.uciekaj(engine.userInput,engine)

    def onCollision(self, engine, gameObject):
        super().onCollision(engine, gameObject)
        if gameObject.group=="Npc":
            self.atakuj(engine.userInput,engine,gameObject)

    def zoomControl(self, input, engine):
        if input[pygame.K_t]:
            self.current_health += 1
        if input[pygame.K_w]:
            engine.setZoom(engine.zoom_factor + 100)
        if input[pygame.K_e]:
            self.rotate += 1
            pygame.transform.rotate(engine.display, - self.rotate)
        if input[pygame.K_r]:
            self.rotate -= 1
            pygame.transform.rotate(engine.display, - self.rotate)

    def controlEntity(self, input):

        if input[pygame.K_DOWN]:
            return self.location.add(0, 1 * self.speed)
        if input[pygame.K_UP]:
            return self.location.add(0, -1 * self.speed)
        if input[pygame.K_LEFT]:
            self.turnLeft()
            return self.location.add(-1 * self.speed, 0)
        if input[pygame.K_RIGHT]:
            self.turnRight()
            return self.location.add(1 * self.speed, 0)
    def rozmawiaj(self,input,engine):
        if input[pygame.K_e]:
            self.sounds = engine.loadSound("Pirat\SzukaszProblemu.mp3")
            self.sounds.play()
    def uciekaj(self,input,engine):
        if input[pygame.K_u]:
            self.location.add(5,5)
    def atakuj(self,input,engine,npc):
        if input[pygame.K_q]:
            npc.destroy()
    def przedstawSie(self,input,engine):
        if input[pygame.K_r]:
            self.sounds = engine.loadSound("Postac\\"+self.user.character+".mp3")
            self.sounds.play()