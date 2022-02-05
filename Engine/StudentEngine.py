import pygame
import os
import traceback
import time
from Engine.GameGroup import GameGroup
import pygame_gui
from audioplayer import AudioPlayer
import os


class Engine:
    def __init__(self):
        self.IS_RUNNING = 1
        self.FPS = 60
        self.WINDOW_SIZE = (1000, 900)
        self.GUI_MANAGER = None
        self.currentTick = 0
        self.toCreateGamesObjects = []
        self.camera = pygame.math.Vector2()
        self.userInput = None
        self.gameEvents = None
        self.screen = None
        self.deltaTime = 0
        self.groups = {}
        self.currentTick = 0
        self.zoom_factor = 1000
        self.display = pygame.Surface(self.WINDOW_SIZE)
        self.ORIG_SURFACE = pygame.Surface(self.WINDOW_SIZE)
        self.CURSOR = None

    def stop(self):
        self.log("Game stop")
        self.IS_RUNNING = 0

    def run(self):
        pygame.init()
        self.log("Game run")
        self.IS_RUNNING = True
        self.GUI_MANAGER = pygame_gui.UIManager((800, 600))
        clock = pygame.time.Clock()
        pygame.mouse.set_visible(False)
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE, pygame.DOUBLEBUF | pygame.RESIZABLE)

        while self.IS_RUNNING:
            try:
                self.gameEvents = pygame.event.get()
                for event in self.gameEvents:
                    self.GUI_MANAGER.process_events(event)
                    if event.type == pygame.QUIT:
                        self.stop()
                        return

                self.userInput = pygame.key.get_pressed()
                self.checkGameObjectsToCreate()

                for groupName in self.groups:
                    group = self.groups[groupName]
                    group.doTick(self)

                self.GUI_MANAGER.update(self.deltaTime)
                self.doGraphic(self.screen)

                self.currentTick = pygame.time.get_ticks()
                self.deltaTime = clock.tick(60) / 1000.0
                print("deltaTime",self.deltaTime)
            except KeyboardInterrupt as manualGameClose:
                break
            except Exception as error:
                self.log("Game stopped due to Exception: " + error)
                traceback.print_exc()
                break
        pygame.quit()

    # =========== Game Engine logic ===================================

    # Initialized all added gameobjects
    def checkGameObjectsToCreate(self):
        for gameObject in self.toCreateGamesObjects:
            gameObject.onEnable(self)
            tag = gameObject.group
            if tag not in self.groups:
                self.groups[tag] = GameGroup()
            self.groups[tag].add(gameObject)

        self.toCreateGamesObjects.clear()

    # Draw all stuff on the screen
    def doGraphic(self, screen):
        screen.fill(255)
        self.display.fill(255)
        self.display = pygame.Surface((self.zoom_factor, self.zoom_factor))
        for groupName in self.groups:
            self.groups[groupName].draw(self.display, self.camera)

        screen.blit(pygame.transform.scale(self.display, screen.get_size()), (0, 0))

        self.GUI_MANAGER.draw_ui(screen)

        if self.CURSOR != None:
            screen.blit(pygame.transform.scale(self.CURSOR, (33,33)),  (pygame.mouse.get_pos()))

        pygame.display.update()

    # =====================================================

    def checkCollisions(self, target, groupName):
        if groupName not in self.groups:
            return

        group = self.groups[groupName]
        colliders = pygame.sprite.spritecollide(target, group, False)
        for collider in colliders:
            target.onCollision(self, collider)
            collider.onCollision(self, target)

    def checkCollision(self, target, groupName):
        if groupName not in self.groups:
            return
        group = self.groups[groupName]
        colliders = pygame.sprite.spritecollide(target, group, False)
        if len(colliders) == 0:
            return
        collider = colliders[0]
        target.onCollision(self, collider)
        collider.onCollision(self, target)

    def checkPixelPerfectCollision(self, target, groupName):
        if groupName not in self.groups:
            return

        group = self.groups[groupName]
        colliders = pygame.sprite.spritecollide(target, group, False, pygame.sprite.collide_mask)
        for collider in colliders:
            target.onCollision(self, collider)
            collider.onCollision(self, target)

    def setCamera(self, x, y):
        self.camera.x = x
        self.camera.y = y

    def setZoom(self, zoom):
        self.zoom_factor = zoom

    def addGameObject(self, gameObject):
        self.toCreateGamesObjects.append(gameObject)

    def playBackgroundMusic(self, path):
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(-1, 0.0)

    def mouseLocation(self):
        return pygame.mouse.get_pos()

    def setZoom(self, zoom):
        if zoom <= 0:
            return

        self.zoom_factor = zoom

    def findGroup(self, groupName):
        return self.groups[groupName]

    def findGameObject(self, name):
        for groupName in self.groups:
            for gameObject in self.groups[groupName]:
                if gameObject.name == name:
                    return gameObject
        return None

    def loadSound(self, path):
        return AudioPlayer('Resources' + os.sep + 'Sounds' + os.sep + path)

    def loadSounds(self, path):
        basePath = 'Resources' + os.sep + 'Sounds' + os.sep + path
        files = os.listdir(basePath)
        result = []
        for file in files:
            if file.find(".") == -1:
                continue
            sound = AudioPlayer(basePath + os.sep + file)
            result.append(sound)
        return result

    def loadImage(self, path):
        image = pygame.image.load('Resources' + os.sep + 'Textures' + os.sep + path + '.png')
        return image

    def loadImages(self, path=''):
        basePath = 'Resources' + os.sep + 'Textures' + os.sep + path
        files = os.listdir(basePath)
        result = []
        for file in files:
            if os.path.isdir(file):
                continue
            image = pygame.image.load(basePath + os.sep + file)
            result.append(image)
        return result

    def setTitle(self, title):
        pygame.display.set_caption(title)

    def setCursorImage(self,path):
        self.CURSOR = self.loadImage(path)

    def getScreenSize(self):
        return self.screen.get_rect()

    def log(self, message):
        current_time = time.strftime("%H:%M:%S", time.localtime())
        print(f"{current_time} [GAME LOG] >> {message}")

    def clearConsole(self):
        print('\n' * 20)
