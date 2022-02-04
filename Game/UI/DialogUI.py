import pygame
from Engine.GameObject import GameObject
import pygame_gui
from Engine.Location import Location
from Game.UI.PixelUIImage import PixelUIImage


class DialogUI(GameObject):
    dialog = None

    def setDialog(self, dialog):
        self.dialog = dialog["dialogs"][0]

    def onEnable(self, engine):
        self.group = "GUI"
        self.rect = pygame.Rect((0, 0), (0, 0))
        self.location = Location(self.rect)
        self.showMessage(self.dialog["messages"][0], engine)

    def showMessage(self, message, engine):
        loc = (100, 550)
        self.createText(message["text"][0], engine, loc)
        self.createOptions(message["options"], engine, loc)

    def createOptions(self, options, engine, loc):
        h = 40
        offset = 10
        p = 0
        for option in options:
            pygame_gui.elements.UIButton(relative_rect=pygame.Rect((loc[0], loc[1] + 100), (100, 400)),
                                         text=option,
                                         manager=engine.GUI_MANAGER)
            p += offset

    def createText(self, message, engine, loc):
        pygame_gui.elements.UITextBox(
            html_text=message,
            relative_rect=pygame.Rect(loc[0], loc[1], 200, 600),
            manager=engine.GUI_MANAGER)
