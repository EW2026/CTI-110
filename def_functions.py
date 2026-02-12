# Attempt at functions


def input_valid(numbers):
    while numbers == "" or not numbers.isdigit():
        numbers = input("Invalid entry, please enter a number only: ")
    
    print("Entry Valid")
    numbers = int(numbers)
    return numbers

def choice_1():
    print("*******************")
    print("Exponent Calculator")
    print("*******************")
    exponent_total, base_number, exp = exponent()
    print()
    print(f"{base_number} raised to the power of {exp} is equal to { exponent_total}")
    print()

def exponent():

    base_number = input_valid(input("Please enter your base number: "))
        
    exp = input_valid(input("Please enter your base exponent: "))
    
    # If input is correct now we calculate
    
    exponent_total = base_number ** exp
    return exponent_total, base_number, exp

def choice_2():
    # This is the code for the addition/subtraction calculator
    print("*******************************************")
    print("-----Addition / Subtraction Calculator-----")
    print("*******************************************")
    # Input and verification rules
    starting_number = input_valid(input("Please enter a starting integer: "))
    
    adding_number = input_valid(input("Please enter an integer to add: "))
    
    subtracting_number = input_valid(input("Please enter an integer to subtract: "))
    
    total_2 = addition_subtraction(starting_number, adding_number, subtracting_number)


def addition_subtraction(starting_number, adding_number, subtracting_number):
        # If inputs are correct, calculates total
    total_2 = starting_number + adding_number - subtracting_number
    print()
    print("Your calculation is:")
    print(f"{starting_number} + {adding_number} - {subtracting_number} is equal to {total_2}")
    print()
    print("Thank You for using my addition and subtraction calculator")
    print()
    return total_2





def display_menu():
    print("******************")
    print("Calculator Program")
    print("******************")
    print("1. Exponent Calculator")
    print("2. Addition // Subtraction")
    print("3. Exit")
        
        
################################ User-Defined Functions end here###############################
        
        
def main():
        
    choice = 0
    
    # While loop runs so long as choice is NOT 3
    while choice != "3":
    
        display_menu()
    
        choice = input("Choose one of the options: ")

        if choice == "1":
            choice_1()
        
        
        if choice == "2":
            choice_2()
# Loops back to selection menu
    
    # While loop ends here
    print("**********************************************************")
    print("Thank you for trying my basic calculator. Have a nice day!")
    print("**********************************************************")
    
main()