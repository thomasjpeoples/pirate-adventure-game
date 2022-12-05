import streamlit as st
import pandas as pd
import requests
import random
import dataclasses

from gamestate import persistent_game_state

HI = 1000
widget_id = (id for id in range(1, 7))

@dataclasses.dataclass
class GameState:
    number: int
    num_guesses: int = 0
    game_number: int = 0
    game_over: bool = False

state = persistent_game_state(initial_state=GameState(random.randint(1, 1000)))

if st.button("More Pirate Adventures, please!"):
    state.number = random.randint(1, HI)
    state.num_guesses = 0
    state.game_number += 1
    state.game_over = False

# Create the rooms on the ship
shrooms={'Name':["", "galley", "lower deck", "upper deck", "captains quarters", "crews quarters", "treasure room"]}
df=pd.DataFrame(shrooms)
df=df.set_index('Name')

# Initialize the game
st.title("Pirate Adventure Game 🏴‍☠️ 🦜 ⚔️")
st.header("_Your_ a pirate on a quest to find treasure on a ship. 🚢 ⚓ 💰 ")
st.text("Pirates are pedants for spelling")
# st.text("The following rooms are available in the ship: ")
# Display the table on the page.
# st.dataframe(shrooms)

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
player_room = ""

# Ask the player which room they want to move to
room = st.selectbox("Which room do you want to move to?", list(df.index), key=state.game_number)
player_room = room

# Main game loop
while not treasure_found and player_room is not None:        
          # Update the player's current room
          if room in rooms:
            player_room = room
            # Print the current room of the player
            if room is not None:
                st.write("You are currently in the", player_room) 
                # Check if the player has found the treasure
                if player_room == "treasure room":
                    treasure_found = True
          else:
            st.write(room, " does not exist on the ship.") 
  
# The player has found the treasure!
st.write("Congratulations, you have found the treasure! 🍾 🎆")
