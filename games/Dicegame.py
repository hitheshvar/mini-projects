# dice game using "random" lib
import random

def roll_dice():
    return random.randint(1, 6)

def play_game():
    player1_name = input("Enter Player 1's name: ")
    player2_name = input("Enter Player 2's name: ")

    player1_score = 0
    player2_score = 0

    rounds = int(input("Enter the number of rounds: "))

    for round in range(1, rounds + 1):
        input(f"Round {round}: {player1_name}, press Enter to roll the dice...")
        player1_roll = roll_dice()
        print(f"{player1_name} rolled a {player1_roll}")

        input(f"Round {round}: {player2_name}, press Enter to roll the dice...")
        player2_roll = roll_dice()
        print(f"{player2_name} rolled a {player2_roll}")

        if player1_roll > player2_roll:
            player1_score += 1
            print(f"{player1_name} wins this round!\n")
        elif player2_roll > player1_roll:
            player2_score += 1
            print(f"{player2_name} wins this round!\n")
        else:
            print("It's a tie for this round!\n")

    print("Game Over!")

    if player1_score > player2_score:
        print(f"{player1_name} wins the game with a score of {player1_score}-{player2_score}")
    elif player2_score > player1_score:
        print(f"{player2_name} wins the game with a score of {player2_score}-{player1_score}")
    else:
        print("It's a tie game!")

#if __name__ == "__main__":
play_game()