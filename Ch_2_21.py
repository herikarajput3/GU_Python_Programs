# Create a dictionary that will accept cricket players name and scores in a match. Also we are retrieving runs by entering the player’s name. 

# Function to create a dictionary of cricket players and their scores
def cricket_scores():
    scores = {}

    # Accept the number of players
    num_players = int(input("Enter the number of players: "))

    # Accept player names and scores
    for i in range(num_players):
        name = input("Enter the player's name: ")
        run = int(input(f"Enter the runs scored by {name}: "))
        scores[name] = run

    # Retrieve runs by entering the player's name
    player_name = input("Enter the player's name to retrieve their runs: ")
    if player_name in scores:
        print(f"{player_name} scored {scores[player_name]} runs.")
    else:
        print(f"No data available for player: {player_name}")

# Example usage
cricket_scores()

