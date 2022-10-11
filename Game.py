from Player import Player
from Opponent import Opponent
import random

class Game():
  # tracks whose turn it is, 0 = player 1 = opponent
  __whoseTurn = None
  __gameOver = False
  __winner = None
  __player = None
  __opponent = None

  def __init__(self, player: Player, opponent: Opponent, cheat=False) -> int:
    self.__player = player
    self.__opponent = opponent
    if cheat == True:
      self.__winner = player
      self.__gameOver = True
    

  def getWinner():
    return self.__winner
  
  def play(self):
    print("The battle is playing out...")
    # store the current teams in mutable lists
    playerTeam = self.__player.getTeam()
    oppTeam = self.__opponent.getTeam()
    # these list will change based on whose turn it is but will always mirror the player / opponent
    attackingTeam = []
    defendingTeam = []
    # player gets to go first
    self.__whoseTurn = self.__player
    # main game loop
    while self.__gameOver == False:
      # each turn, every ship will attack every other enemy ship
      # if one player has 2 ships and the attacker has 3, on of the players shipps will be attacked twice
      # attack phase
      if self.__whoseTurn == self.__player:
        attackingTeam = playerTeam
        defendingTeam = oppTeam
      else:
        attackingTeam = oppTeam
        defendingTeam = playerTeam
      for i in range(len(attackingTeam)):
        # print(f"the team lengths are {len(attackingTeam)} - {len(defendingTeam)}")
        # check if we have a winner
        if len(defendingTeam) == 0:
          self.__gameOver = True
          if self.__whoseTurn == self.__player:
            self.__winner = self.__opponent
          else:
            self.__winner = self.__player
          break
        # each ship on attacking teams attacks a random ship on the other team to keep it simple
        defendingShip = defendingTeam[random.randint(0, len(defendingTeam) - 1)]
        defendingShip.shields -= attackingTeam[i].atkDamage
        # check if the defending ship was destroyed and if so, remove it from the ship
        if defendingShip.shields < 0:
          defendingTeam.remove(defendingShip)
          # give some feedback when a ship is destroyed
          if self.__whoseTurn == self.__player:
            print("💥💥💥💥 You destroyed an enemy ship 💥💥💥💥")
          else:
            print("💥💥 The enemy destroyed one of your ships 💥💥")
        # the game is still going, next turn
        if self.__whoseTurn == self.__player:
          self.__whoseTurn = self.__opponent
        else:
          self.__whoseTurn = self.__player

    # assign the winner
    if type(self.__winner) == Player:
      winner = "You"
    else:
      winner = "The enemy"
    print(f"{winner} won this time!")
    return 
      