# Evan Westcott
# 20260303
# P3LAb
# Use division and branching for coin algorithm


# Get a float input from the user and assign to change 
    # Variable Creation

change = float(input("How much change do you need?: $"))

    # Multiplies change by 100 to move decimal 2 places to the right
change = int(change * 100)

    # Creates the variables for the change
DOLLARS= 100
QUARTERS = 25
DIMES = 10
NICKLES = 5
PENNIES = 1

    # Determine number of dollars in change using floor division
dollars = change // DOLLARS

    # Determine number of quarters based on the modulus of dollars using floor division
balance = change % DOLLARS
quarters = balance // QUARTERS

    # Determine number of dimes based on the modulus of dollars and quarters using floor division
balance = balance % QUARTERS
dimes = balance // DIMES

    # Determine number of nickles based on the modulus of dollars, quarters and dimes using floor division
balance = balance % DIMES
nickles = balance // NICKLES

    # Determine number of pennies based on the modulus of dollars, quarters, dimes and pennies using floor division
balance = balance % NICKLES
pennies = balance // PENNIES


    # Using if statements, this section prints only the statements needed and whether or not they are plural
print()
if dollars > 0:
    if dollars > 1:
        print(f"You require {dollars} Dollars")
    else:
        print("You require 1 Dollar")
        
if quarters > 0:
    if quarters > 1:
        print(f"You require {quarters} Quarters")
    else:
        print("You require 1 Quarter")
        
if dimes > 0:
    if dimes > 1:
        print(f"You require {dimes} Dimes")
    else:
        print("You require 1 Dime")

if nickles > 0:
    if nickles > 1:
        print(f"You require {nickles} Nickles")
    else:
        print("You require 1 Nickle")

if pennies > 0:
    if pennies > 1:
        print(f"You require {pennies} Pennies")
    else:
        print("You require 1 Penny")

if change == 0:
    print("No change required")

