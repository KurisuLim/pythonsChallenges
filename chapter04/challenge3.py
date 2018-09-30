print("""
Challenge #3
Improve 'World Jumble' so that each word is paried with a hint.
The player should be able to see the hint if he or she is stuck.
Add a scoring system that rewards players who solve a jumble
without asking for the hint.
""")

import random

WORDS = ("toffer","Icecream", "python", "kurisu", "lim")
word = random.choice(WORDS)
correct = word

jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print(
"""
        Welcome to World Jumble 2.0!

    Unscramble the letters to make a word.
 (Press the enter key at the prompt to quit.)

"""
)

print("The jumble word is: ", jumble)

guess = input("\nYour guess: ")
counter = 0
while guess != correct and guess != "":
    if (counter >= 3):
        print("Here is a hint: ", jumble)
        counter += 1
        guess = input("\nYour guess: ")
    else:
        print("Sorry, that's not it.")
        counter += 1
        guess = input("\nYour guess: ")

if guess == correct and counter < 3:
    print("That's it! You guessed it! You got 100% on this! \n")
elif guess == correct and counter >= 3:
    print("You got it right but, you already saw the hint!\nYou got a participation badge.")

print("Thanks for playing.")

input("\n\nPress the enter key to exit.")
