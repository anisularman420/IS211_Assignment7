import argparse
import random

class Player:
    def __init__(self, number):
        self.number = number
        self.score = 0

def roll_die():
    return random.randint(1, 6)

def play_game(num_players):
    players = [Player(i + 1) for i in range(num_players)]
    player_index = 0

    while True:
        player = players[player_index]

        print(f"Player {player.number}'s turn.")
        turn_score = 0
        while True:
            decision = input(f"Roll (r) or Hold (h): ").lower()
            if decision == 'r':
                roll = roll_die()
                print(f"Player {player.number} rolled a {roll}.")
                if roll == 1:
                    print(f"Player {player.number} rolled a 1. Turn score reset.")
                    turn_score = 0
                    break
                else:
                    turn_score += roll
                    print(f"Player {player.number}'s turn score: {turn_score}")
            elif decision == 'h':
                player.score += turn_score
                print(f"Player {player.number} chose to hold.")
                print(f"Player {player.number}'s total score: {player.score}")
                if player.score >= 100:
                    print(f"Player {player.number} wins with a score of {player.score}!")
                    return
                break
            else:
                print("Invalid input. Please enter 'r' to roll or 'h' to hold.")

        player_index = (player_index + 1) % num_players

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--numPlayers', type=int, default=2, help='Number of players in the game')
    parser.add_argument('--numGames', type=int, default=1, help='Number of games to play')
    args = parser.parse_args()

    num_players = args.numPlayers
    num_games = args.numGames

    for game in range(num_games):
        print(f"Game {game + 1}")
        play_game(num_players)
        print("End of Game")

if __name__ == '__main__':
    main()
