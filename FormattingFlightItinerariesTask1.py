#Objective: The aim of this assignment is to deepen your understanding of tuples in Python.

#Task 1: Formatting Flight Itineraries Create a Python function that takes a list of tuples as an argument. Each tuple contains information about a flight itinerary: (traveler_name, origin, destination).
#The function should format and return a string that lists each itinerary. For example, if the input is `[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]`, the output should be a string formatted as:

#"Itinerary 1: Alice - From New York to London
# Itinerary 2: Bob - From Tokyo to San Francisco"

#Writing code for FormattingFlightItinerariesTask1

#Instantiating itinerary as list to appened new data
itinerary_list = []

#Instantiating function to take in Tuples into itinerary_list list
def flight_itinerary(plans):
#Created loop to catch for repeated answers, all other answers are flexible strings and accepted
    while True:
#Instantiating items within tuples as name origin and destination with formatted string for itinerary representation
        name = input("Please enter the name of the person for the itinerary: ") + " -"
        origin = "From " + input("Please enter where the person is coming from: ")
        destination = "to " + input("Please enter where the person is going to: ")

#Creating variable name for each tuple created
        plan = (name, origin, destination)

#Catching for tuples already in itinerarly_list list and same to and from destination by passing plans as itinerary_list as defined in main() function
        if plan in plans:
            print("Itinerary already exists.")
        elif origin == destination:
            print("Where the person is coming from cannot be the same as where they are going to.")
        else:
            itinerary_list.append(plan)
            print("Itinerary added successfully")
            re_main()

#Instantiating exit_itenerary function to exit out of menu options after printing full itinerary list
def exit_itinerary():
    print("Here is your Full Flight Itinerary:\n")
#Instantiated element append to start loop with number defined from 0 + 1 to define each loop as individual itinerary
    element_added = 0
#Created for loop to convert each tuple into string with a counting variable defined as individual itinerary
    for element in itinerary_list:
        str = ''
        for item in element:
#Adding each item in element to itself to avoid item replacement, replaces instead with itself plus new data
            str = str + item + " "
        element_added += 1
#Defining each item in itinerary_list to the full itinerary per item in element and printing full list of itinerarys with example formatting and printing
        full_list = "Itinerary " + f"{element_added}" + ": " + f"{str}"
        print(full_list)

    print("\nThank you for using Flight Itineraries Menu.")
    exit()

#Instantiating menu function that allows for user operator entry and uses while loop which rejects all other entries aside from int 1-2
def main():
    plans = set()
    print(f'''\nWelcome to the Flight Itineraries Menu\n       Menu:
        1. Add a flight plan
        2. Quit\n''')
    while True:
        operator = input("Please choose menu choice:\n")
        if operator == "1":
            plans = itinerary_list
            flight_itinerary(plans)
            break
        elif operator == "2":
            exit_itinerary()
            break
        else:
            print ("Apologies, entry must be either 1 or 2.\n\n")

#Instantiating re_menu function without Welcome message that allows for user operator entry and uses while loop which rejects all other entries aside from int 1-2
def re_main():
    plans = set()
    print(f'''\nFlight Itineraries Menu\n       Menu:
        1. Add a flight plan
        2. Quit\n''')
    while True:
        operator = input("Please choose menu choice:\n")
        if operator == "1":
            plans = itinerary_list
            flight_itinerary(plans)
            break
        elif operator == "2":
            exit_itinerary()
            break
        else:
            print ("Apologies, entry must be either 1 or 2.\n\n")

#Calling main function to run
main()
