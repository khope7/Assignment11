#Task 1: Library System Enhancement Sharpen your skills in managing and modifying data within tuples and lists.
#
#Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this system by adding new books and ensuring no duplicates.
#
#Existing Library Data:
#
#library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
#- Add functionality to insert new books into `library`. Ensure that adding a duplicate book is handled appropriately.




#Writing code for LibrarySystemEnhancementTask1

#Instantiating library list
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

#Instantiating first function to show defaulted library list calling elements of nested tuple list and printing in user friendly format
def first():
    print("\nHere is your current list of books")
    print("Book 1: " + f"{library[0][0]}" + " " f"{library[0][1]}")
    print("Book 2: " + f"{library[1][0]}" + " " f"{library[1][1]}")

#Instantiating function to take in Tuples into itinerary_list list
def add_books(bookshelf):
#Created loop to catch for repeated answers, all other answers are flexible strings and accepted
    while True:
#Instantiating items within tuples as name origin and destination with formatted string for itinerary representation
        name = input("Please enter the name of the book: ")
        author = input("Please enter the author of the book: ")

#Creating variable name for each tuple created
        full_book = (name, author)

#Catching for tuples already in itinerarly_list list and same to and from destination by passing plans as itinerary_list as defined in main() function
        if full_book in bookshelf:
            print("Book already exists.")
        else:
            library.append(full_book)
            print("Book added successfully")
            main()

#Instantiating exit_itenerary function to exit out of menu options after printing full itinerary list
def exit_library():
    print("Here is your Full Library:\n")
#Instantiated element append to start loop with number defined from 0 + 1 to define each loop as individual itinerary
    element_added = 0
#Created for loop to convert each tuple into string with a counting variable defined as individual itinerary
#https://www.geeksforgeeks.org/python-program-to-convert-a-tuple-to-a-string/# for reference
    for element in library:
        str = ''
        for item in element:
#Adding each item in element to itself to avoid item replacement, replaces instead with itself plus new data
            str = str + item + " "
        element_added += 1
#Defining each item in itinerary_list to the full itinerary per item in element and printing full list of itinerarys with example formatting and printing
        full_list = "Book " + f"{element_added}" + ": " + f"{str}"
        print(full_list)
    print("\nThank you for using the Library Menu.")
    exit()

#Instantiating menu function that allows for user operator entry and uses while loop which rejects all other entries aside from int 1-2
def main():
    bookshelf = set()
    print(f'''\nWelcome to the Library Menu\n       Menu:
        1. Add a book
        2. Quit\n''')
    while True:
        operator = input("Please choose menu choice:\n")
        if operator == "1":
            bookshelf = library
            add_books(bookshelf)
            break
        elif operator == "2":
            exit_library()
            break
        else:
            print ("Apologies, entry must be either 1 or 2.\n\n")


#Calling first function for initial default list print
first()

#Calling main function to run
main()