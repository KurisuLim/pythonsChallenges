print(
"""
Challenges
1. Create a list of legal and illegal variable names. Describe why
each is either legal or ilegal. Next, create a list of a "good" and
"bad" legal variable names. Describe why each is either good or bad choice
for a variable name.
2. Write a program that allows a user to enter his or her two
favorite food by joining the original food names together.
3. Write a Tipper programmer where the user enters a restaurant
bill total. The program should then display two amounts: a 15 percent tip
and a 20 percent tip.
4. Write a Car Salesman program where the user enters the
base price of a car. The program should add on a bunch of extra fees
such as tax, license, dealer prep, and destination charge. Make
tax and licence a percent of the base price. The other fees should
be set values. Display the actual price of the car once all the extra are
applied.
"""
)

input("\nPress Enter to Begin")
print("""
Challenge #1:
legal variables list:
- numberOne
- notString
- doNotFloat

It's legal because its easy to read and it describe what that varaible
is for. Not only that we use camel case and its not too long.

illegal variable list:
- _underscore
- 123Number
- IMALLCAPS
- h-y-p-h-e-n

The first illegal _underscore is declaring it s a class.
The second 123Number makes the compiler crash, because it cannot
decide it its a number or a identifier.
The IMALLCAPS represents its a constant variable
The hyphens are harder to read
"""
)
input("\nPress Enter to begin Challenge 2")
print("Challenge #2:")
favFood1 = str(input("What is your first favorite food? "))
favFood2 = str(input("What is your second favorite food? "))
output = favFood1 +" & " + favFood2
print("Okey, your favorite foods are", output, ".")

input("\nPress Enter to begin Challenge 3")
print("Challenge #3:")
bill = float(input("Please enter the total amount of the Bill: $"))
tip10 = bill * .10
tip20 = bill * .20
bill10 = bill + tip10
bill20 = bill + tip20
print("The amount of 10% tip: $",tip10)
print("The amount of 20% tip: $",tip20)
print("Total bill with 10% tip: $", bill10)
print("Total bill with 20% tip: $", bill20)
input("\nPress Enter to begin Challenge 4")
print("Challenge #4:")
carBase = float(input("Please enter the base price of the car? $"))
carTax = carBase * .08
carLicense = carBase * .05
carDealerPrep = float(input("Please enter the dealer prep: $"))
carDestCharge = float(input("Please enter the destination charge: $"))
totalAmount = carBase + carTax + carLicense  + carDealerPrep + carDestCharge
print("Car Base Price: $", carBase ,"\n",
      "Car Tax: $", carTax, "\n",
      "Car License: $", carLicense, "\n",
      "Car Dealer Prep: $", carDealerPrep, "\n",
      "Car Destination Charge: $", carDestCharge, "\n",
      "Total Amount is Due: $", totalAmount
)

input("\nPress Enter to Exit")




