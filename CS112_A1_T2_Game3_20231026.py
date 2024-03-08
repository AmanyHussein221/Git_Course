# File : CS112_A1_T2_Game3_20231026.py
# Purpose : Subtract a square game. We have number of coins and 2 players. Each player take a square number and the player who removes the last coin wins.
# Author : Amany Hussein Mousa
# ID : 20231026
import math
import random

# Check if the number is a perfect square
def is_perfect_square(num):
    return num >= 0 and math.isqrt(num) ** 2 == num

# Check if the number is valid number
def get_valid_move(player, remaining_coins):
    while True:
        try:
            move = int(input(f'Player {player}: Please take a square number of coins: '))
        except ValueError:
            print('Invalid input! Please enter a valid integer.')
            continue

        if is_perfect_square(move) and 0 < move <= remaining_coins:
            return move
        else:
            print('Invalid move! Please take a valid square number of coins.')

# welcome message to the user and definition of the game
print('Welcome to subtract a square game. Players take turns removing coins using only square numbers. Last one to remove a coin wins.')

# Ask the user if they want to choose the total number of coins or have a random total
user_choice = input('Do you want to choose the total number of coins (enter "1") or have a random total (enter "2"): ')
if user_choice == '1':
    # User chooses the total number of coins
    number_of_all_coins = int(input('Please enter the total number of coins: '))
else:
    # User wants a random total number of coins
    number_of_all_coins = random.randint(10, 1000)
    print(f'The total number of coins is randomly set to: {number_of_all_coins}')

while number_of_all_coins > 0:
    # Player 1's move
    move1 = get_valid_move(1, number_of_all_coins)
    number_of_all_coins -= move1
    print(f'Player 1 took {move1} coins. Now, we have: {number_of_all_coins}')

    # Check if player 1 won
    if number_of_all_coins == 0:
        print('Player 1 is the winner!')
        break

    # Player 2's move
    move2 = get_valid_move(2, number_of_all_coins)
    number_of_all_coins -= move2
    print(f'Player 2 took {move2} coins. Now, we have: {number_of_all_coins}')

    # Check if player 2 won
    if number_of_all_coins == 0:
        print('Player 2 is the winner!')
        break