import streamlit as st
import pandas
import requests

# Initialize the game
st.title("Pirate Adventure Game 🏴‍☠️ 🦜 ⚔️")
st.header("You are a pirate on a quest to find treasure on a ship. 🚢 ⚓ 💰 ")

# Initialize the rooms on the ship
rooms = {
  "galley": (0, 0),
  "lower deck": (0, 1),
  "upper deck": (0, 2),
  "captains quarters": (1, 0),
  "crews quarters": (1, 1),
  "treasure room": (1, 2)
}

# Initialize variables for the game
treasure_found = False
player_room = "galley"

# Main game loop
while not treasure_found:
  # Print the current room of the player
  st.write("You are currently in the", player_room)
  
# Ask the player which room they want to move to
  if st.button("Move to galley", key="move_g"):
    player_room = "galley"
  if st.button("Move to lower deck", key="move_ld"):
    player_room = "lower deck"
  if st.button("Move to upper deck", key="move_ud"):
    player_room = "upper deck"
  if st.button("Move to captains quarters", key="move_cq"):
    player_room = "captains quarters"
  if st.button("Move to crews quarters", key="move_cq"):
    player_room = "crews quarters"
    
  # Check if the player has found the treasure
  if player_room == "treasure_room":
    treasure_found = True
  
# The player has found the treasure!
st.write("Congratulations, you have found the treasure! 🍾 🎆")
