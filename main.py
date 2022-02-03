from Engine.StudentEngine import Engine
from Game.Player import Player
from Game.Npc import Npc
from Game.Tile import Tile
from Game.UI.PlayerUI import PlayerUI
engine = Engine()
engine.setTitle("Super student RPG Game")
for i in range(0, 50):
    engine.addGameObject(Tile(i*16, i*16))
engine.addGameObject(Player())
for i in range(0,1):
    engine.addGameObject(Npc())


engine.addGameObject(PlayerUI())
engine.run()
