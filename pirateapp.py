import streamlit as st
import pandas
import requests

# Initialize the game
st.title("Pirate Adventure Game 🏴‍☠️ 🦜 ⚔️")
st.header("You are a pirate on a quest to find treasure on a ship. 🚢 ⚓ 💰 ")

# Initialize the rooms on the ship
rooms = {
  "galley": (0, 0),
  "lower_deck": (0, 1),
  "upper_deck": (0, 2),
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
  room = st.selectbox("Which room do you want to move to?", ["galley", "lower_deck", "upper_deck", "captain's_quarters", "crew's_quarters"], key="room_select")

  # Update the players current room
  if room in rooms:
    player_room = room
  else:
    st.write("That room does not exist on the ship 😡")

  # Check if the player has found the treasure
  if player_room == "treasure_room":
    treasure_found = True

# The player has found the treasure!
st.write("Congratulations, you have found the treasure! 🍾 🎆")
