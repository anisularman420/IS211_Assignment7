import random
import sys
class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.total_score = 0
        self.turn_score = 0

# Two blank lines here

def roll_die():
    return random.randint(1, 6)


def take_turn(player):
    print(f"Player {player.player_id}'s turn.")
    while True:
        player_choice = input("Roll (r) or Hold (h): ").lower()
        if player_choice == 'r':
            roll = roll_die()
            if roll == 1:
                print(f"Player {player.player_id} rolled a 1. Turn score reset.")
                player.turn_score = 0
                break
            else:
                player.turn_score += roll
                print(f"Player {player.player_id} rolled a {roll}.")
                print(f"Player {player.player_id}'s turn score: {player.turn_score}")
        elif player_choice == 'h':
            player.total_score += player.turn_score
            player.turn_score = 0
            print(f"Player {player.player_id} chose to hold.")
            print(f"Player {player.player_id}'s total score: {player.total_score}")
            break
        else:
            print("Invalid input. Please enter 'r' to roll or 'h' to hold.")

def play_game(num_players, players):
    current_player_index = 0

    while True:
        current_player = players[current_player_index]
        take_turn(current_player)

        if current_player.total_score >= 100:
            print(f"Player {current_player.player_id} wins with a score of {current_player.total_score}!")
            break

        current_player_index = (current_player_index + 1) % num_players

    # Reset game state after the game ends
    for player in players:
        player.total_score = 0
        player.turn_score = 0

def main():
    num_players = int(input("Enter the number of players: "))
    num_games = int(input("Enter the number of games: "))

    for game in range(num_games):
        print(f"Game {game + 1}")
        players = [Player(i) for i in range(1, num_players + 1)]
        play_game(num_players, players)
        # Reset game state
        print("Game over. Resetting scores and game state.")
        for player in players:
            player.total_score = 0
            player.turn_score = 0

if __name__ == "__main__":
    main()
