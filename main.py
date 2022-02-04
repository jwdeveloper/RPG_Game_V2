from Engine.StudentEngine import Engine
from Game.Player import Player
from Game.Npc import Npc
from Game.Tile import Tile
from Game.UI.PlayerUI import PlayerUI
from Game.Audio.AudioManager import AudioManager
from Game.Pirates.Pirate import Pirate
from Game.ExampleLevel import ExampleLevel
from Game.Loaders.QuestsLoader import QuestLoader
from Game.Loaders.NPCLoader import NPCLoader
from Game.Loaders.ItemsLoader import ItemsLoader
from Game.UI.DialogUI import DialogUI
from Game.Camera import Camera
from Game.Pirates.Sapling import Sapling

a = NPCLoader()
b = a.load()

a = ItemsLoader()
b = a.load()

a = QuestLoader()
b = a.load()

engine = Engine()
engine.setTitle("Super student RPG Game")
engine.setCursorImage("UI\\cursor")

engine.addGameObject(Camera())
level = ExampleLevel()
level.create(engine)

engine.addGameObject(Player())
engine.addGameObject(Npc())
engine.addGameObject(Pirate())
engine.addGameObject(Sapling())
a = DialogUI()
a.setDialog(b[0])
engine.addGameObject(a)
engine.addGameObject(AudioManager())
engine.run()
