# Evan Westcott
# 20260210
# P1HW1
# Allow user input to calculate different functions

# This is the code to select the operations you can do
is_running = True
# Table of Contents
while is_running:
    print("******************")
    print("Calculator Program")
    print("******************")
    print("1. Exponent Calculator")
    print("2. Addition // Subtraction")
    print("3. Exit")


    # Gives user the input field for choice of which operation to use
    choice = input("Please enter choice (1-3): ")
    
    if choice == "1":
        # This is the code for the exponent calculation
        print("-----------Exponent Calculation------------")

        # Input and verification rules
        base_number = input("Please enter your base number: ")
        if base_number == "" or not base_number.isdigit():
            base_number: str = input("Invalid entry, please enter an integer as the base value: ")
        else:
            base_number = int(base_number)
        exp = input("Please enter your exponent: ")
        if exp =="" or not exp.isdigit():
            exp = input("Invalid entry, please enter an integer as the exponent: ")
        else:
            exp = int(exp)

        # If inputs are correct, calculates total
        total = base_number ** exp
        print()
        print("Your calculation is:")
        print(F"{base_number} raised to the power of {exp} is {total}")
        print()
        print("Thank You for using my exponent calculator")
        print()
        # Loops back to selection menu
    
    elif choice == "2":
        # This is the code for the addition/subtraction calculator
        print()
        print("-----Addition / Subraction Caclulator-----")
        print()

        # Input and verification rules
        starting_number = input("Please enter an integer to add: ")
        if starting_number == "" or not starting_number.isdigit:
            starting_number = input("Invalid entry, please enter a starting integer: ")
        else:
            starting_number = int(starting_number)

        adding_number = input("Please enter an integer to add: ")    
        if adding_number == "" or not adding_number.isdigit:
            adding_number = input("Invalid entry, please enter an integer to add: ")
        else:
            adding_number = int(adding_number)

        subtracting_number = input("Please enter an integer to subtract: ")    
        if subtracting_number == "" or not subtracting_number.isdigit:
            subtracting_number = input("Invalid entry, please enter an integer to subtract: ")
        else:
            subtracting_number = int(subtracting_number)

        # If inputs are correct, calculates total
        total_2 = starting_number + adding_number - subtracting_number
        print()
        print("Your calculation is:")
        print(f"{starting_number} + {adding_number} - {subtracting_number} is equal to {total_2}")
        print()
        print("Thank You for using my addition and subtraction calculator")
        print()
        # Loops back to selection menu

    # Allows user to exit the program
    elif choice == "3":
        is_running = False

    # Prevents user from making an invalid choice and loops back to the selection menu
    else:
        print()
        print("That is not a valid choice")
        print()
print()
print("Thank you for trying my basic calculator. Have a nice day!")
print()
