# Evan Westcott
# 20260211
# P1HW2
# Allows users to budget for their vacations

############################# Function Definitions ############################################

def menu():
    print("***************************************")
    print("Welcome to the travel budget calculator")
    print("***************************************")
    print("Please Choose from the following options:")
    print("1 for yes")
    print("2 for no")

    
# Choice Validation
def character_valid(character):
    while character == "" or not character.isalpha():
        character = input("Input invalid, please enter your vacation spot: ")

    print("Thank you for your input")
    return character.lower

def number_valid(number):
    while number == "" or not number.isdigit():
        number = input("please enter a valid number: ")

    print("Thank you for your entry")
    return int(number)

    


# Trip Calculation Function
def trip():

    print("*******************************************************************************************")
    print("Please enter the city in which you wish to travel to only. Do not include spaces or commas.")
    print("*******************************************************************************************")
    destination = character_valid(input("Where would you like to go?: "))
    
    budget = number_valid(input("Please enter your estimated budget: "))
    
    transportation_cost = number_valid(input("Please enter your estimated cost to arrive at your destination: "))
   
    room = number_valid(input("What is the estimated cost of your hotel stay?: "))
    
    food = number_valid(input("What do you plan to spend on food and drinks?: "))
  
    souvenir_cost = number_valid(input("What do you plan to spend on souvenirs?: "))

    total = transportation_cost + room + food + souvenir_cost

    print("**************************")
    print(f"Your budget is ${budget}")
    print(f"You wish to go to {destination}")
    print(f"The total of your estimated costs is ${total}")

    
    if budget > total:
        print("************************************")
        print("You are under your budget.😁😁😁😁")
        print("************************************")

    elif budget == total:
        print("*****************************************************************************************************************************")
        print("Your budget is equal to your total expenditures, it is reccomeneded that you either budget more or spend less money😬😬😬😬")
        print("*****************************************************************************************************************************")

    else:
        print("**********************************************************************************************************")
        print("Your total expenditures exceeds your budget. It is recommended that you spend less or do not go.😟😟😟😟")
        print("**********************************************************************************************************")
    
    return budget, destination, transportation_cost, room, food, souvenir_cost


######################################## End of User Functions #############################################

def main():
    
    # Starts an infinite Loop
    choice = 0

    # Keeps loop going unless option "2" is entered
    while choice != "2":

        # Shows Menu
        menu()

        choice = input("Do you wish to continue? y/n: ")
        while choice == "" or not choice.isdigit():
            choice = input("please enter a valid choice: ")
        
        print("Let's budget for your trip!")
        
        
        # Runs trip function
        if choice == "1":

            trip()
            
    # Exits Loop
    else:
        print("************************************************************")
        print("Thank you for trying my budget calcaulator. Have a nice day!")
        print("************************************************************")

main()

