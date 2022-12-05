import streamlit
import pandas
import requests

# Initialize the game
streamlit.title("Welcome to the Pirate Adventure game!")
streamlit.header('You are a pirate on a quest to find treasure.')

# Initialize variables for the game
treasure_found = False
treasure_x_coord = 0
treasure_y_coord = 0
player_x_coord = 0
player_y_coord = 0

# Main game loop
while not treasure_found:
  # Print the current location of the player
  print("You are currently at coordinates:", player_x_coord, player_y_coord)

  # Ask the player which direction they want to move
  direction = input("Which direction do you want to move? (north, south, east, west) ")

  # Update the player's coordinates based on the direction they chose
  if direction == "north":
    player_y_coord += 1
  elif direction == "south":
    player_y_coord -= 1
  elif direction == "east":
    player_x_coord += 1
  elif direction == "west":
    player_x_coord -= 1

  # Check if the player has found the treasure
  if player_x_coord == treasure_x_coord and player_y_coord == treasure_y_coord:
    treasure_found = True

# The player has found the treasure!
print("Congratulations, you have found the treasure!")
