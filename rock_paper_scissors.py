"""
Program to emulate the classic Rock Paper Scissors game.
"""

import os
os.system('clear')

import random
from data import rock, paper, scissors

images = [rock, paper, scissors]
game_on = True

print("WELCOME TO ROCK PAPER SCISSORS!!!")

while game_on:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
    if user_choice in [0, 1, 2]:
        print(f"You chose:\n{images[user_choice]}")

        computer_choice = random.randint(0, 2)
        print(f"Computer chose:\n{images[computer_choice]}")

        if user_choice == 0 and computer_choice == 2:
            print("You win!")
        elif user_choice == 2 and computer_choice == 0:
            print("You lose!")
        elif user_choice > computer_choice:
            print("You win!")
        elif user_choice < computer_choice:
            print("You lose!")
        else:
            print("It's a draw!")
        
        user_choice = input("Would you like to play again? Type 'Y' for yes, 'N' for no: ").lower()
        if user_choice == 'y':
            os.system('clear')
            continue
        else:
            game_on = False
    else:
        print("Invalid input, try again!")
