#Guess My Number You vs Computer
#
#In this version of the Guess My Number, you got to guess
#the right number before the computer does.

import random

number = random.randint(1,10)
playerGuess  = 0;
playerWins = 0;
pcGuess = 0;
pcWins = 0;
playerGuess = int(input("Take a guess: "));
                        
while playerWins != 1 or pcWins != 1:
#Players turn

    if playerGuess == number:
        print(playerGuess," is a correct guess...")
        playerWins = 1;
    else:
        if playerGuess > number:
            print("Lower...\n")
        else:
            print("Higher...\n");
            
    if pcGuess != number:
         pcGuess = random.randint(1,10)
    else:
        print("PC got it first")
        pcWins = 1;
        
    print("\nPlayer pick the number: ", playerGuess);
    print("Pc pick the number: ", pcGuess);
    playerGuess = int(input("\nTake a guess: "))
    
if playerGuess == number and pcGuess == number:
    print("A tie breaker!")
elif playerGuess == number and playerGuess != pcGuess:
    print("\nCongrats Player, you beat our PC!");
    print("The number was ", number)
else:
    print("\nComputer win! You suck!");
    print("The number was ", number)

input("\nPress Enter to Exit")
