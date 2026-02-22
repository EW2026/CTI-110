# Importing math library from Python
import math

# Evan Westcott
# 20260217
# P2Lab1
# calculations for circle based on user input

# Menu for loop
def menu():
    print()
    print("*******************************")
    print("Welcome to my circle calculator")
    print("*******************************")
    print()

# user input variable    
def calc():
    radius = input("What is the radius of the circle?: ")
    while radius == "" or not radius.isdigit():
        radius = input("Invalid entry, please enter a radius: ")

    print(f"Your radius is: {radius} ")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^")

    # Calculation for circle  
    radius = float(radius)
    diameter = 2 * radius
    circumference = 2 * math.pi * radius
    area = math.pi * math.pow(radius, 2)
    
    # Shows Answers
    
    print("-----------------------------------------------")
    print(f"The diameter of your circle is {diameter:.1f}.")
    print("---------------------------------------------------------")
    print(f"The circumference of your circle is {circumference:.2f}.")
    print("---------------------------------------------------------")
    print(f"The area of your circle is {area:.3f}.")
    print("---------------------------------------")






################################### End of functions ################################

def main():

# Creates the loop
    choice = "true"
    
    # Allows Loop as long as the answer to choice does not equal "n"
    
    while choice != "n":
        menu()
        calc()
        
        
        choice = input("Would you like to calculate another circle?: (y/n)").lower()
        
        # This while loop forces user to input a single letter
        
        while choice == "" or not choice.isalpha() or not len(choice) == 1:
            
            #This allows for user to exit the while loop by entering a single letter
            choice = input("Invalid entry, please choose (y/n): ").lower()
             
    
    # If choice does equal "n" then the user exits the loop
    print("*********************************")
    print("Thank you for using my calculator")
    print("*********************************")



main()