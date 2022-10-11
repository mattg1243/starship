from Player import Player, constructors
import random

# this class defines the simulated opponent the user will be playing against
class Opponent(Player):

  # overwritting the Player constructor to create a team at random
  def __init__(self):
    self.__team = [
      s for s in [
        constructors[random.randint(1, 3)], constructors[random.randint(1, 3)],
        constructors[random.randint(1, 3)]
      ]
    ]

  def getTeam(self):
    return self.__team