from Engine.StudentEngine import Engine
from Game.Player import Player
from Game.Npc import Npc
from Game.Audio.AudioManager import AudioManager
from Game.Pirates.Pirate import Pirate
from Game.Camera import Camera
from Game.Pirates.Theodor import Theodor
from Game.Loaders.Login import UserManager
from Game.Levels.ShipLevel import ShipLevel
from Game.Pirates.Pirate import PirateKacper
from Game.Pirates.Pirate import Captin



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
engine.addGameObject(Pirate())
engine.addGameObject(Theodor())
engine.addGameObject(Captin())
engine.addGameObject(PirateKacper())
engine.run()
