import pygame
from Game.Settings import *
from Engine.GameObject import GameObject
import pygame_gui
from Engine.Location import Location
from Game.UI.PixelUIImage import PixelUIImage

class PlayerUI(GameObject):

    def onEnable(self, engine):
        self.group = "GUI"
        self.rect = pygame.Rect((0, 0), (0, 0))
        self.location = Location(self.rect)
        self.player = engine.findGameObject("player")
        self.test = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 275), (300, 50)),
                                                 text='Click to give XP',
                                                 manager=engine.GUI_MANAGER)

        asd = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(233, 233, 200, 50),
            manager=engine.GUI_MANAGER)
        asdad = PixelUIImage(
            relative_rect=pygame.Rect(444, 444, 160, 160),
            manager=engine.GUI_MANAGER, image_surface=engine.loadImage("Wall"))
        self.progress = pygame_gui.elements.UIScreenSpaceHealthBar(
            relative_rect=pygame.Rect(556, 555, 1111, 1111),
            manager=engine.GUI_MANAGER)
        self.progress.set_sprite_to_monitor(self.player)


        text_box = pygame_gui.elements.UITextBox(
            html_text="This is an <effect id=test>EARTHQUAKE</effect>",
            relative_rect=pygame.Rect(100, 100, 200, 50),
            manager=engine.GUI_MANAGER)
        text_box.set_active_effect(pygame_gui.TEXT_EFFECT_BOUNCE, effect_tag='test')

