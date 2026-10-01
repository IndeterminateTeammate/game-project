#Lab 1
#Group Number: 1
#Author: Sean Fay
#Date: 27 Sept 2026

import guessing 
import rock_paper_scissor

def main():
    """
    This is the main function that runs the game selection menu. 
    It allows the user to choose between playing a guessing game, 
    rock-paper-scissors, or exiting the program.
    Author: Sean Fay
    """
    while True:
        print('=============================')
        print('Would you like to play a game?')
        print('Choose wisely!')
        print('1. Guessing Game')
        print('2. Rock Paper Scissors')
        print('3. Exit')
        print('=============================')
        choice = input('Please input 1, 2, or 3: ')
        if choice == '1':
            guessing.guessing_game()
        elif choice == '2':
           rock_paper_scissor.rock_paper_scissor()
        elif choice == '3':
            print('Thanks for playing! Toodles!')
            break
        else:
            print('Invalid input. Choose better.')
if __name__== '__main__':    
    main()  