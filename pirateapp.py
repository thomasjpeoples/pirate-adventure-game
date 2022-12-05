# Initialize the game
print("Welcome to the Pirate Adventure game!")
print("You are a pirate on a quest to find treasure on a ship.")

# Initialize the rooms on the ship
rooms = {
  "galley": (0, 0),
  "lower deck": (0, 1),
  "upperdeck": (0, 2),
  "captain's quarters": (1, 0),
  "crew's quarters": (1, 1),
  "treasure room": (1, 2)
}

# Initialize variables for the game
treasure_found = False
player_room = "galley"

# Main game loop
while not treasure_found:
  # Print the current room of the player
  print("You are currently in the", player_room)

  # Ask the player which room they want to move to
  room = input("Which room do you want to move to? (galley, lower deck, upper deck, captain's quarters, crew's quarters) ")

  # Update the player's current room
  if room in rooms:
    player_room = room
  else:
    print("That room does not exist on the ship.")

  # Check if the player has found the treasure
  if player_room == "treasure_room":
    treasure_found = True

# The player has found the treasure!
print("Congratulations, you have found the treasure!")
