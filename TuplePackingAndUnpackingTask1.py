#Task 1: Customer Order Processing Refine your skills in tuple unpacking by managing customer orders.

#Problem Statement: You are given a list of tuples, each representing a customer's order. Each tuple contains the customer's name, the product ordered, and the quantity. Your task is to unpack each tuple and print the order details in a user-friendly format.

#Sample Order Data:

#orders = [
#    ("Alice", "Laptop", 1),
#    ("Bob", "Camera", 2),
#    # More orders...
#]

#Write a function to iterate over the list of orders. - Unpack each tuple in the list and format the details for display.


#Writing code for TuplePackingAndUnpackingTask1

#Instantiating orders tuple list
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]

#Instantiating menu function that allows for user operator entry and uses while loop which rejects all other entries aside from int 1-3
def menu():
    print(f'''\nHello, please choose to add to list, print list, or exit\n       Menu:
        1. Add to list
        2. Print list
        3. Quit\n''')
#Instantiating while loop to allow for user re-entry
    while True:
        operator = input("Please choose menu choice:\n")
        if operator == "1":
            add_to_list()
            break
        elif operator == "2":
            print_list()
            break
        elif operator == "3":
            exit_run()
            break
        else:
            print ("Apologies, entry must be between 1 and 3.\n\n")

#Instantiating re_menu function to give user updated message unique from welcome message
def re_menu():
    print(f'''Please choose to add to list, print list, or exit\n       Menu:
        1. Add to list
        2. Print list
        3. Quit\n''')
    while True:
        operator = input("Please choose menu choice:\n")
        if operator == "1":
            add_to_list()
            break
        elif operator == "2":
            print_list()
            break
        elif operator == "3":
            exit_run()
            break
        else:
            print ("Apologies, entry must be between 1 and 3.\n\n") 

#Instantiating add_to_list function that creates entries for each item within listed tuple and appends new tuple entry back into orders list
def add_to_list():
#Instantiating empty tuple for element packing
    new_entry = ()
#Instantiating elements from user entry
    name = input("\nPlease enter name for entry: ")
    product = input("Please enter product for person: ")
#Instantiating while loop with try except block to catch for any entry less than 0 int and any entry not an int
    while True:
        try:
            quantity = int(input("Please enter quantity of product: "))
            if quantity < 0:
                print("Apologies, quantity must be a full number.")
            else:
                break
        except ValueError:
            print("Apologies, quantity must be a number greater than 0")
#Packs elements into new_entry tuple and appends to orders list
    new_entry = (name, product, quantity)
    orders.append(new_entry)
#Printing list append confirmation and sends user back into main operation menu without Hello message
    print("Entry for " f"{name}" + " has been added to the list")
    re_menu()

#Instantiating print_list function to display updated entries
def print_list():
    entry = 0
    print("Here is your entered list:\n\n")
#Unpacking each item to iterate from each tuple within orders list and running until all tuples are printed
#https://medium.com/@leonardkinyanjui/pythons-nested-tuple-unpacking-87d844ea548a for reference
    for (name, product, quantity) in orders:
#Instantiating count for each tuple within list
        entry += 1
#Printing unpacked tuple in user friendly format
        print("Entry " + f"{entry}" + ". " + "Name: " + name + " - " + "Product: " + product + " - " + "Quantity: " + f"{quantity}")
#Returning to menu operator without hello message
    re_menu()

#Instantiating exit_run function to exit run after printing Thank you message
def exit_run():
    print("Thank you")
    exit()
        
#Calling menu to run
menu()