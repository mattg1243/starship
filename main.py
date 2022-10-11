from Player import Player
from Opponent import Opponent
from Game import Game
from Battleship import BattleShip
from Medical import MedicalShip
from Transport import TransportShip

# create the player and opponent instances
player = Player()
opponent = Opponent()
# initialize the game
# hint: if you change cheat to True, youll win every time!
game = Game(player, opponent, cheat=False)
# play the game
game.play()

# TODO: the game seems to be working, although feedback is not 
# displaying consistently when a ship is blown up...