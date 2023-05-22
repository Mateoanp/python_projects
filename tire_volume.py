'''
Many companies wish to understand the needs and wants of their customers more deeply so 
the company can create products that fill those needs and wants. One way to understand 
customers more deeply is to record the values entered by customers while they are using a 
program and then to analyze those values. One common way to record values is for a program 
to store them in a file.
'''

# creating variables
print()
w = int(input("Enter the width of the tire in mm (ex 205): "))
a = int(input("Enter the aspect ratio of the tire (ex 60): "))
d = int(input("Enter the diameter of the wheel in inches (ex 15): "))
import math
pi = math.pi

# calculations
v = (math.pi * (w**2) * (a*(w * a + 2540 * d))) / 10000000000

# getting date from computer's operating's system
from datetime import datetime 
date = datetime.now()

# printing the approx volume in liters
print(f"\nThe approximate volume is {v:.2f} liters\n")

# buying tires
buy = input("Would you like ot buy tires with the dimention that you entered? (yes/no) ")
# open text file for appending
with open('volumes.txt', 'at') as volumes:
    if buy.lower() == "yes":
        # appending value incluidng phone number
        phone = input("\nWhat is your phone number? ")
        print(f"{date:%Y-%m-%d}, {w}, {a}, {d}, {v:.2f}, {phone}\n", file=volumes)
        print("\nThank you, an specialist will get in contact with you soon.\n")
    elif buy.lower() == "no":
        # appending values without phone number
        print(f"{date:%Y-%m-%d}, {w}, {a}, {d}, {v:.2f}\n", file=volumes)
        print("Thank you!")
    else:
        print("Incorrect answer")
        # appending values without phone number
        print(f"{date:%Y-%m-%d}, {w}, {a}, {d}, {v:.2f}\n", file=volumes)
        

