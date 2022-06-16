#!/usr/bin/env python3

"""
Project Statement
The guessing game has four errors. Find and correct the errors so that
the user can set an upper limit to the range of numbers, it gets a random
number in that range, and allows the user to guess until correct. It should
display 'too high' or 'too low' hints.
-------------------------------------------------------------------------
When you fix the program, upload the working program and list, as comments,
the errors you found and fixed.
Error 1: count was not specified, so it was called before it was specied
Error 2:main is missing an : after the main()
Error 3:play game has no functions to pass into it in main. Had to add limit. ex: play_game(limit)
Error 4: play game had an >= number in the 1st elif. It would never get to the 2nd statement to finish the game. 
"""

import random

def display_title():
    print("Guess the number!")
    print()

def set_limit():
    print("Enter the upper limit for the range of numbers: ")
    limit = int(input())
    return limit

def play_game(limit):
    number = random.randint(1, limit)
    count = 0
    print("I'm thinking of a number from 1 to " + str(limit) + "\n")
    while True:
        guess = int(input("Your guess: "))
        if guess < number:
            print("Too low.")
            count += 1
        elif guess > number:
            print("Too high.")
            count += 1
        elif guess == number:
            count += 1
            print("You guessed it in " + str(count) + " tries.\n")
            return

def main():
    display_title()
    again = "y"
    while again.lower() == "y":
        limit = set_limit()
        play_game(limit)
        again = input("Play again? (y/n): ")
        print()
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()

