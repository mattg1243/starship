from Super import SuperShip
from Battleship import BattleShip
from Medical import MedicalShip
from Transport import TransportShip
from typing import List

# putting constructors into a dictionary so they can be called
# based on the numerical input from the user while picking team
constructors = {1: BattleShip(), 2: MedicalShip(), 3: TransportShip()}


class Player():
  # team list will store the players ships
  __team: List[SuperShip] = []

  # constructor will prompt the user to create their team
  def __init__(self):
    print(
      """Welcome to my Starship Battle game! Please pick your team by entering 
    a number between 1 and 3, 3 times. Each entry corresposponds to a different type
    of ship. For instance:
    1 = Battle Ship
    2 = Medical Ship
    3 = Transport Ship
    Entering 1 2 3 will give you a team with one of each ship.""")
    teamStr = input("Go ahead and enter your team now: ")
    # split the input and convert chars to ints
    teamList = [int(i) for i in teamStr.split(" ")]
    # make sure user entered valid numbers
    if min(teamList) < 1 or max(teamList) > 3:
      print(
        "You have entered an invalid number during team selection. Programming exiting, try again"
      )
      return -1
    # input is valid, create team
    for i in range(3):
      self.__team.append(constructors[teamList[i]])

  def getTeam(self):
    return self.__team
    