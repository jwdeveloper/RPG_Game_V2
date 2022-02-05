from Engine.StudentEngine import Engine
from Game.Player import Player
from Game.Npc import Npc
from Game.Audio.AudioManager import AudioManager
from Game.Pirates.Pirate import Pirate
from Game.ExampleLevel import ExampleLevel
from Game.Levels.ShipLevel import ShipLevel
from Game.Camera import Camera
from Game.Pirates.Sapling import Sapling





engine = Engine()
engine.setTitle("Super student RPG Game")
engine.setCursorImage("UI\\cursor")

engine.addGameObject(Camera())
level = ShipLevel()
level.create(engine)

engine.addGameObject(Player())
engine.addGameObject(Npc())
engine.addGameObject(Pirate())
engine.addGameObject(Sapling())
engine.addGameObject(AudioManager())
engine.run()
