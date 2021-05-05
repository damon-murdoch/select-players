# Operating System Library
import os

# Operating System Path Library
import os.path

# System Library (For sys.argv)
import sys

# For Comma-Seperated Value Files
import csv

# For getting random numbers
import random

class Player:

  def __init__(self,list):

    # Define the name of the player
    self.name = list[0]

    # Number of match wins player has
    self.wins = int(list[1])
    
    # Number of match losses player has
    self.loss = int(list[2])

    # If the player is available this week or not
    # If this is 0 (false), the player will not be picked
    self.available = bool(list[3])

    # Total number of games the player has played
    # Used as the primary selector for picking players
    self.games = self.wins + self.loss

    # Win/Loss score for the player
    # Used as tiebreaker for players on same number of games
    self.score = self.wins - self.loss
  
  # Result of str(this)
  def __str__(self):
    return self.name + ": " + \
      str(self.wins) + "W " + \
      str(self.loss) + "L (" + \
      str(self.games) + ")"

  # Result of otherwise casting to string
  def __repr__(self):

    # Return the str(x) method
    return self.__str__()

# select_players(count: int): list
# Return the list of player names which 
# should be selected for this week
# Count is an optional parameter that sets
# the number of players which should be picked
def select_players(players, count=6):

  # Temporary unsorted list
  unsorted = []

  # Iterate over each player provided
  for player in players:

    # If the player is available
    if player.available:

      # Add the player to the list
      unsorted.append(player)

  # Sort the list using a lambda function
  # Sorting function prioritises players who have 
  # played less than the others, then sorts the rest
  # by their win/loss ratio

  selected = sorted(unsorted, key=lambda x: (x.games,-x.score))[:count]

  # Return list of selected players
  return selected

# If this file is being executed
if __name__ == '__main__': 

  # List for storing users
  players = []

  # Count variable, for how
  # many players should be selected
  count = 6

  # Dereference the arguments
  args = sys.argv

  # If there is more than 1 argument
  if len(args) > 1:

    # Set the count variable 
    # to the first argument
    count = int(argv[1])

  # Check for the players.csv file
  dirname = os.path.dirname(__file__)

  # Get the path of the players.csv file
  filename = os.path.join(dirname, 'players.csv')

  # Check if the players file exists
  if (os.path.isfile(filename)):
    
    # File exists
    with open(filename) as f:

      # Parse the csv  file
      csv_read = csv.reader(f, delimiter=',')

      # Iterate over each row in the csv
      for row in csv_read:

        # Generate a player object
        player = Player(row)

        # Append the player to the players list
        players.append(player)

      # Select the players who should be picked
      selected = select_players(players,count)

    # Print the ordered list first
    print("Players (Ordered):",selected)

    # Shuffle the selected list
    rand = random.shuffle(selected)

    print("Order to Submit:")

    # Iterate over selected players
    for sel in range(len(selected)):

      # Print the name of the player
      print(sel,selected[sel].name)

  else:
    # File does not exist
    print("File Missing:",filename,"\nPlease create it with contents in the following format:\nName,Wins,Losses,Available (e.g. Scrubbs,0,0,1)")