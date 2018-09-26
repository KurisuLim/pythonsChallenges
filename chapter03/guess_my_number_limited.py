#Guess My Number Limited Style
#
#The computer picks a random number between 1 and 100
#The player tries to guess it and the computer lets
#the player know if the guess is too high, too low
#or right on the money. As well as how many tries left

import random
print("\tWelcome to 'Guess My Number'!");
print("\t\tLimited Style");
print("Try to guess it less than 5 attemps");

#set the initial values of the variables
number = random.randint(1, 100)
tries = 5;
turns = 5;
print("Your attemps: ", tries);
guess = int(input("Take a guess: "))
tries -= 1
turns -= 1

while turns != 0:
    if guess == number:
        print("\nCongrats you guess it right!")
        turns = 0
    else:
        if guess > number:
            print("Lower...")
        else:
            print("Higher...")

        print("You have ", tries, " left")
        guess = int(input("Take a guess: "))
        tries -= 1
        turns -= 1


if turns == 0 and tries != 0:
    print("The number was ", number)
    print("You have guest it on ", tries, "attemps left.")
else:
    print("\nYou have run out of attemps. Please try again next time")
    print("The number was ", number)

input("\n\nPress the enter key to exit.")


        
    
