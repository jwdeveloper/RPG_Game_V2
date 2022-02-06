from Engine.GameObject import GameObject
import pygame


class Entity(GameObject):
    rotate = 1
    speed = 3
    stats = {}

    def onEnable(self, engine):
        self.right = None
        self.left = None
        self.stats['speed'] = 10
        self.stats['health'] = 100
        self.stats['maxHealth'] = 100
        self.stats['energy'] = 50
        self.hpBar = EntityHP()
        self.hpBar.setEntity(self)
        self.hpBar.setActive(True)
        engine.addGameObject(self.hpBar)
        self.audioPlayer = EntityAudioPlayer()

    def playSound(self, sound):
        self.audioPlayer.addSoundToQueue(sound)

    def turnLeft(self):
        if self.left is None:
            self.left = pygame.transform.flip(self.image, True, False)
        self.image = self.left

    def turnRight(self):
        if self.right is None:
            self.right = pygame.transform.flip(self.image, False, False)
        self.image = self.right

    def onTick(self, engine):
        engine.checkCollision(self, "wall")
        self.audioPlayer.checkQueue()

    def onCollision(self, engine, gameObject):

        if gameObject.group == "wall":
            x = self.location.lastX
            y = self.location.lastY
            self.location.set(x, y)
        else:
            d = self.location.direction(gameObject.location)
            self.location.add(d[0], d[1])


class EntityHP(GameObject):
    entity = None
    offSet = 1
    sprites = 0

    def onEnable(self, engine):
        self.group = "entity-helath-bar"
        self.images = engine.loadImages("UI\\HP")
        self.setImage(self.images[0])
        self.sprites = len(self.images)

    def onTick(self, engine):
        if self.entity == None:
            return
        x = self.entity.location.X()
        y = self.entity.location.Y() - self.location.height() - self.offSet
        self.location.set(x, y)
        self.image = self.getImage()

    def getImage(self):
        health = self.entity.stats["health"]
        maxHealth = self.entity.stats["maxHealth"]

        if health == 0:
            return self.images[self.sprites - 1]
        else:
            index = self.sprites - int(10 * (health / maxHealth))
            return self.images[index]

    def setEntity(self, entity):
        self.entity = entity


class EntityAudioPlayer:

    def __init__(self):
        self.playingQueue = []
        self.currentSound = None
        self.isPlaying = False
        self.maxTime = 200
        self.currentTime = 0

    def addSoundToQueue(self, sound):
        self.playingQueue.append(sound)

    def checkQueue(self):

        if self.currentSound is None:
            if len(self.playingQueue) == 0:
                self.currentTime = 0
                self.isPlaying = False
                return
            self.currentSound = self.playingQueue.pop(0)
            if self.currentSound is None:
                return
            else:
                self.currentSound.play()
                self.isPlaying = True
                return
        else:
            self.currentTime += 1
            if self.currentTime > self.maxTime:
                self.currentTime = 0
                self.currentSound = None
