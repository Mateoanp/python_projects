print()
w = int(input("Enter the width of the tire in mm (ex 205): "))
a = int(input("Enter the aspect ratio of the tire (ex 60): "))
d = int(input("Enter the diameter of the wheel in inches (ex 15): "))
import math
pi = math.pi

v = (math.pi * (w**2) * (a*(w * a + 2540 * d))) / 10000000000

print(f"\nThe approximate volume is {v:.2f} liters\n")

