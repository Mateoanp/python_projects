print("\nWelcome to the Shopping Cart Program!")

      
items = []
prices = []
action = None
while action != 5:
    print('''
Please select one of the following: 
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit''')
    action = int(input("Please enter an action: "))

   # add item
    if action == 1:
        add = input("What item would you like to add? ")
        price = float(input("What is item's price? "))
        items.append(add)
        prices.append(price)
        print(f"'{add}' has been added to the cart.")

    # view cart
    elif action == 2:
        print("\nThe contents of the shopping cart are:")
        for i in range(len(items)):
            print(f"{i + 1}. {items[i]} - ${prices[i]:.2f}")

    # remove item
    elif action == 3:
        print("\nThe items in the list are:")
        for i in range(len(items)):
            print(f"{i + 1}. {items[i]} - ${prices[i]:.2f}")
        print(f"Total number of items: {len(items)}")
        item_remove = int(input("\nWhich item would you like to remove? ")) - 1
        if item_remove <= len(items):
            items.pop(item_remove)
            prices.pop(item_remove)
            print("\nItem removed.")
            print(f"\nNew total number of items: {len(items)}")
            print("Updated list of items:")
            for i in range(len(items)):
                print(f"{i + 1}. {items[i]} - ${prices[i]:.2f}")
        else:
            print("Sorry, that is not a valid item number.")
    elif action == 5:
        print("Thank you. Goodbye")

    # compute total
    
    elif action == 4:
        total = 0 
        for price in prices:
            total += price
        print(f"\nThe total price of the items in the shopping cart is ${total:.2f}")
    else:
        print("Enter a valid option")
    

