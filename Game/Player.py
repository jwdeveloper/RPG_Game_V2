from Engine.GameObject import GameObject
import pygame
from Game.Entity import Entity
from Game.UI.PlayerUI import PlayerUI
from Engine import Math
import pygame_gui


class Player(Entity):

    def onEnable(self, engine):
        super().onEnable(engine)
        self.setImage(engine.loadImage("Postacie\\Klasy\\Bard"))
        self.ui = PlayerUI()
        self.group = "player"
        self.name = "player"
        self.stats["exp"] = 20
        self.location.add(50, 30)

    def onTick(self, engine):

        self.controlEntity(engine.userInput)
        self.zoomControl(engine.userInput, engine)
        self.stickToCamera(engine)
        super().onTick(engine)

    def onCollision(self, engine, gameObject):
        engine.clearConsole()
        print(gameObject.name)
        super().onCollision(engine, gameObject)

    def stickToCamera(self, engine):
        camera = engine.camera
        l1 = self.location.clone().set(camera.x, camera.y)
        l2 = self.location.clone()
        result = Math.lerp(l1, l2, 0.3)
        engine.setCamera(result.X(), result.Y())

    def zoomControl(self, input, engine):
        if input[pygame.K_t]:
            self.current_health += 1
        if input[pygame.K_q]:
            engine.setZoom(engine.zoom_factor - 10)
            engine.clearConsole()
        if input[pygame.K_w]:
            engine.setZoom(engine.zoom_factor + 10)
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
