from Engine.GameObject import GameObject
from Game.Tile import Tile
import pygame

class Water(Tile):

    speed = -1
    def onTick(self, engine):
       
        if self.location.X() < -600:
            self.location.set(1400, self.location.Y())
        else:
            self.location.add(self.speed, 0)



