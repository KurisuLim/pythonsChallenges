#Flip a Coin Program
#
#When the program runs, it will have a while loop running 100 times.
#And each time it does run, there will be a random generator number
#between 1 or 2. If the random number is 1 then it's head. If
#the random generator number is 2 then its tails. And at the end of
#program, we will display how many head and tails has been flip.
#
import random;

heads = 0;
tails = 0;
input("\nReady for a coin toss? 100 times style?\nPress Enter to Start\n")
for x in range(1,100):
    number = random.randint(1,2);
    if number == 1:
        heads+=1
    elif number == 2:
        tails+=1

print("Head toss flip: ", heads);
print("Tails toss flip: ",tails);
input("\n\nDid you have fun?Hope so, Press Enter to Exit")
