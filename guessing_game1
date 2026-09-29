#Lab 1
#Group #1
#Authors: AARAV ROY
#Date: 9//22/2026

import random
def guessing_game():
    """This is my guessing game. PLayers guess a number.It allows you to rank up in difficulty, IF you win. The way the difficulty increases the range increases by 10"""
    max_num=75
    max_attempts=10
    attempts = 0
    random_num = random.randint(1, max_num)
    while True:
        guess =(input("Guess a number between 1 and " + str(max_num) + " say quit to exit, you have " + str(max_attempts-attempts) + " attempts:"))
        if guess == "quit":
            print("Thanks for playing! Goodbye.")
            break
        elif guess!= "quit":
            guess = int(guess)
        if guess != random_num:
            if attempts > max_attempts:
                print("OH NOOOO!!!!! You've reached the maximum number of attempts. The correct number is:", random_num)
                continue
            if guess < 1 or guess > max_num:
                        print("Please guess a number between 1 and " + str(max_num) + ".")
            if guess+10== random_num:
                        print("You're very close! Try again.")
            if guess-10== random_num:
                        print("You're very close! Try again.")
            if guess+5== random_num:
                        print("You're SUPER close!!! Try again.")
            if guess-5== random_num:
                        print("You're SUPER close!!! Try again.")
            if guess > random_num:
                print("Too high! Try again.")
            elif guess < random_num:
                print("Too low! Try again.")
            attempts += 1
        if guess == random_num:
            print("Congratulations! You guessed the correct number:", random_num)
            attempts=0
            difficulty = input("Do you want to ramp up the difficulty? (yes/no): ")
            if difficulty.lower()=="no":
                break
            elif difficulty.lower() == "yes":
                max_num+=10
if __name__== "__main__":
    print("Welcome to my guessing game")
    guessing_game()
