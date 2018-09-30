print("""
Challenge #1
Write a program that counts for the user. Let the user enter the
starting number, the ending number, and the amount by which to count.
""")
number = 0
start = None
finish = None

print("\n\nHello welcome to Challenge 1!\n")

print("Please enter a value.")
print("Press the enter key at 'Begin' to exit.")

while start != "":
    start = input("\nStart: ")

    if start:
        start = int(start)

        finish = int(input("Finish: "))

        number = finish - start

        print("number[", start, ":", finish, "] is", end=" ")
        print("total count would be: ", number)

input("\n\nPress the enter key to exit.")

