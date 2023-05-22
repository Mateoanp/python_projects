print()
items = int(input("Enter the number of items: "))
items_per_box = int(input("Enter the number of items per box: "))
import math
boxes = math.ceil(items / items_per_box)

print(f"\nFor {items} items, packing {items_per_box} items in each box, you will need {boxes} boxes.\n")