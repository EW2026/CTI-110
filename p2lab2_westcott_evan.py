# Evan Westcott
# 20260219
# P2Lab2
# Practice with dictionaries

# Import math
import math

################## Set up dictionaries ############################

car = {"camaro": 18.21,
        "prius": 52.36,
        "model s": 110,
        "silverado": 26}
        
        
############### Dictionary Complete ##############################
# Variables to distinguish between the model s from the rest

# Dispay keys to user

cars = car.keys()
print(cars)
print()

# User input to pull info from dictionary

print()
user_car = input("Enter vehicle to find out its MPG/MPE: ")
user_car= user_car.lower()
print()

mpg_type = "mpg"
if user_car == "model s":
    mpg_type = "mpge"
    
unit_type = "gallon(s)"
if user_car == "model s":
    unit_type = "recharge(s)"



# Function Shows MPG/MPE for user

user_car_mpg_mpe = car[user_car]

print(F"Your car, the {user_car}, gets an estimated {user_car_mpg_mpe} {mpg_type}")

# Asks user how far they will drive the car

user_travel_distance = float(input(f"How many miles do you plan to drive the {user_car}?: "))

# Calculation for gallons/recharges required rounded up

units = user_travel_distance / user_car_mpg_mpe
units = math.ceil(units)

# Shows user how many times they will have to refuel/ recharge
if user_car != "model s":
    print(f"You will have to use an estimated {units} {unit_type} to make your trip.")
else:   
    print(f"You will have to recharge an estimated {units} time(s) to make your trip.")
