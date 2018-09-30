print("""
Challenge #2
Create a program that gets a message from the user and then
prints it backwards.
""")

print("\nIn this solution we used the revered() method.")

message = str(input("\nPlease enter a message: "))
print("\nThe message you input: ", message, "\n" )
reverseWord = ""
for i in reversed (message):
    print(i)
    reverseWord += i

print("\nThe reverse word is: ", reverseWord)

print("\nNow lets try '[::-1]' slicing trick to reverse the message.")

input('\nPress Enter to continue.')

word = input("\nPlease enter a word or sentence: ")
print("\nThe word or sentence you input: ", word)
print("\nReversing using word[::-1]")
print("\nReverse word or sentence you input: ", word[::-1])

input("\nPress Enter to Exit.")
