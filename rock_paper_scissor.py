#Lab 1
#Group #1
#Authors: Colton Feige
#Date: 9//22/2026

import random

def rock_paper_scissor(): 
    contine = 'Y'
    while contine.upper() == 'Y':
        'User input '
        choices = ["rock", "paper", "scissors"]
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        'dectecs a Invalid choice'
        while user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            user_choice = input("Choose rock, paper, or scissors: ").lower()
        'computer choice'
        computer_choice = random.choice(choices)
        'prints both user and Computer choice'
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        'prints the output'
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            print("You win!")
        else:
            print("You lose!")
        'ask the user if they want to continue using this program'
        contine = input("Do you want to continue using this program? (Y/N) ")




if __name__ == "__main__":
    rock_paper_scissor()