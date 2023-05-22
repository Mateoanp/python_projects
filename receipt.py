# import csv
# # Import the datetime class from the datetime
# # module so that it can be used in this program.
# from datetime import datetime

# # Call the now() method to get the current
# # date and time as a datetime object from
# # the computer's operating system.
# current_date_and_time = datetime.now()


# def main():
    
#         products_dict = read_dictionary("products.csv", 0)
#         #print(products_dict)

#         # number of items variable
#         num_products = 0

#         # define subtotal variable
#         subtotal_total = 0

#         #define tax variable
#         tax_total = 0

#         #define total variable
#         total = 0

#         #print store name
#         print("Inkom Emporium")

#         with open("request.csv", "rt") as request_file:
#             reader = csv.reader(request_file)
#             next(reader)
#             print()
#             #print("\nRequested Items")

#             for row in reader:
#                 product_number = row[0]
#                 quantity = int(row[1])

#                 product_info = products_dict.get(product_number)
                
#                 if product_info:
#                     product_name = product_info[1]
#                     product_price = float(product_info[2])
#                     # total_price = product_price * quantity

#                     print(F"{product_name}: {quantity} @ {product_price}")
#                     # number of items counts
#                     num_products += quantity

#                     #calculate subtotal
#                     subtotal_total += quantity * product_price

#                     #calculate tax
#                     tax_total = subtotal_total * 0.06

#                     #calcualte total
#                     total = subtotal_total + tax_total
        

#         #print items' quantity
#         print()
#         print("Number of products:", num_products)
#         print(f"Subtotal: {subtotal_total:.2f}")
#         print(f"Sales Tax: {tax_total:.2f}")
#         print(f"Tax total: {total:.2f}")
#         print("\nThank you for shopping at the Inkom Emporium.")
#         # Use an f-string to print the current
#     # day of the week and the current time.
#         print(f"{current_date_and_time:%A %I:%M %p}")   



# def read_dictionary(filename, key_column_index):
#     """Read the contents of a CSV file into a compound
#     dictionary and return the dictionary.

#     Parameters
#         filename: the name of the CSV file to read.
#         key_column_index: the index of the column
#             to use as the keys in the dictionary.
#     Return: a compound dictionary that contains
#         the contents of the CSV file.
#     """
    
#     compound_dictionary = {}
#     with open(filename, "rt") as products_file:
#         reader_file = csv.reader(products_file)
#         next(reader_file)

#         for row in reader_file:
#             key = row[key_column_index]
#             value = row
#             compound_dictionary[key] = value

#     return compound_dictionary

# # products_dict = read_dictionary("products.csv", 0)
# # print(products_dict)  

# if __name__ == "__main__":
#     main()


import csv
from datetime import datetime

def read_dictionary(file_name, key_index):
    products_dict = {}
    try:
        with open(file_name, "rt") as file:
            reader = csv.reader(file)
            for row in reader:
                key = row[key_index]
                products_dict[key] = row
    except FileNotFoundError:
        print(f"File not found: {file_name}")
    except PermissionError:
        print(f"Permission denied: {file_name}")
    
    return products_dict

def main():
    try:
        products_dict = read_dictionary("products.csv", 0)
        #print(products_dict)

        # number of items variable
        num_products = 0

        # define subtotal variable
        subtotal_total = 0

        # define tax variable
        tax_total = 0

        # define total variable
        total = 0

        # print store name
        print("Inkom Emporium")

        try:
            with open("request.csv", "rt") as request_file:
                reader = csv.reader(request_file)
                next(reader)
                print()
                # print("\nRequested Items")

                for row in reader:
                    product_number = row[0]
                    quantity = int(row[1])

                    try:
                        product_info = products_dict[product_number]
                    except KeyError as key_err:
                        print(type(key_err).__name__, key_err)
                        print(f"Error: Unknown product ID in the request.csv file: '{product_number}'")
                        return
                    product_name = product_info[1]
                    product_price = float(product_info[2])
                    # total_price = product_price * quantity

                    print(f"{product_name}: {quantity} @ {product_price}")
                    # number of items counts
                    num_products += quantity

                    # calculate subtotal
                    subtotal_total += quantity * product_price

                    # calculate tax
                    tax_total = subtotal_total * 0.06

                    # calculate total
                    total = subtotal_total + tax_total

                    

        except FileNotFoundError:
            print("Request file not found")
        except PermissionError:
            print("Permission denied: request.csv")

        # print items' quantity
        print()
        print("Number of products:", num_products)
        print(f"Subtotal: {subtotal_total:.2f}")
        print(f"Sales Tax: {tax_total:.2f}")
        print(f"Tax total: {total:.2f}")
        print("\nThank you for shopping at the Inkom Emporium.")
        current_date_and_time = datetime.now()
        # Use an f-string to print the current
        # day of the week and the current time.
        print(f"{current_date_and_time:%A %I:%M %p}")

    except FileNotFoundError:
        print("Products file not found")
    except PermissionError:
        print("Permission denied: products.csv")

if __name__ == "__main__":
    main()


