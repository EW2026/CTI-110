# Evan Westcott
# 20260203
# P1LAB1 
# Provide an 2 inputs for the user to enter first and last name, then print Hello, name! Welcome to CTI 110


# Code for printing hello name! welcome to CTI 110
    # This provides the user input and ensures the user inputs something
fname = input("Please enter your first name: ")
while fname == "" or not fname.isalpha():
        fname = input("Please enter your first name here: ")
lname = input("input invalid, please reenter your first name correctly: ")
while lname == "":
      print("You failed to enter your name")
      lname = input("Please enter your last name here: ")


   
    # This prints the message so long as the user inputs their name
print()
print(f"Hello {fname} {lname}! Welcome to CTI 110!😁😁😁")
print()    