print(
"""
Challenge #4
Create a game where the computer picks a random word and
the player has to guess that word. The computer tells the
player how many letters are in the word. Then the player gets
five chances to ask if a letter is in the word. The computer can
only respond with 'yes' or 'no' .Then, the player must guess
the word.
"""
)

input("\nPress Enter to Begin...")
#imports module
import random
import os
import sys
import time

screen_width = 100

# Player Setup
class player:
    def __init__(self):
        self.name =""
        self.game_over = False
myPlayer = player()

# create a sequence of words to choose from
WORDS = ("java" ,"css","html","python","ruby","javascript")
# picks one word randomly from the sequnce
word = random.choice(WORDS)
# create a variable to use later to see if the guess is correct
correct = word

def title_screen_selection():
    question = "Please, choose an option.\n"
    for character in question:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    option = input("> ")

    while option not in ["1","2"]:
        message = "Please enter a valid command: 1 or 2"
        for character in message:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        option = input("\n> ")
        if option == ("1"):
            game_start()
        elif option == ("2"):
            print("Thank you for playing.")
            sys.exit()

    
def title_screen():
    
    print(
        """
            ##############################################
            #                                            #
            #      Welcome to Guess the Word Game!       #
            #                                            #
            ##############################################

                            [1] Play
                            [2] Exit 
        """
        )

    title_screen_selection()

def prompt():
    print("\nThis is not done yet!")
    input("\nPress enter to exit")
    myPlayer.game_over = True

def main_game_loop():
    while myPlayer.game_over is False:
        prompt()

def game_start():
    os.system("clear")

#Gets the player name
    question = "Hello, what is your name?\n"
    for char in question:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer.name = player_name



#Introduction
    message = "Welcome, " + player_name + "!"

    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

    os.system("clear")
    print(
        """
                LETS BEGIN!
        """
        )
    main_game_loop()


  
title_screen()
