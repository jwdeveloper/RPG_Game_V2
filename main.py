from Engine.StudentEngine import Engine
from Game.Player import Player
from Game.Npc import Npc
from Game.Audio.AudioManager import AudioManager
from Game.Pirates.Pirate import Pirate
from Game.ExampleLevel import ExampleLevel

from Game.UI.DialogUI import DialogUI
from Game.Camera import Camera
from Game.Pirates.Sapling import Sapling
from Game.Loaders.Login import UserManager
from Game.Levels.ShipLevel import ShipLevel


engine = Engine()
engine.setTitle("Super student RPG Game")
engine.setCursorImage("UI\\cursor")

level = ShipLevel()
level.create(engine)


engine.addGameObject(Camera())
engine.addGameObject(AudioManager())

# Player
manager = UserManager()
manager.load()
user = manager.login()
player = Player()
player.setUser(user)
engine.addGameObject(player)



# NPC
engine.addGameObject(Npc())
engine.addGameObject(Pirate())
engine.addGameObject(Sapling())

engine.run()
