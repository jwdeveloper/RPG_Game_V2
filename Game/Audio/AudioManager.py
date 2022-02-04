from Engine.GameObject import GameObject
import pygame
from Engine.Location import Location


class AudioManager(GameObject):


    def onEnable(self, engine):
        self.group = "Audio"
        self.rect = pygame.Rect((0, 0), (0, 0))
        self.location = Location(self.rect)
        self.backGroundTrack = engine.loadSound("Music\Background.mp3")
        self.backGroundTrack.volume = 10
        self.backGroundTrack.play()

        self.backGroundMusic = engine.loadSound("Music\Instumental.mp3")
        self.backGroundMusic.volume = 5
        self.backGroundMusic.play()


