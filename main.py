from Engine.StudentEngine import Engine
from Game.Player import Player
from Game.Npc import Npc
from Game.Tile import Tile
from Game.UI.PlayerUI import PlayerUI
from Game.Audio.AudioManager import AudioManager
from Game.Pirates.Pirate import Pirate
from Game.ExampleLevel import ExampleLevel

engine = Engine()
engine.setTitle("Super student RPG Game")
engine.setCursorImage("UI\\cursor")
level = ExampleLevel()
level.create(engine)

engine.addGameObject(Player())
engine.addGameObject(Npc())
engine.addGameObject(Pirate())

# engine.addGameObject(PlayerUI())
engine.addGameObject(AudioManager())
engine.run()
