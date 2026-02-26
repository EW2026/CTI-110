# Evan Westcott
# 20260226
# P2HW2
# Using user input to create and search a list along with width formatting

from decimal import Decimal, ROUND_HALF_UP


############################## Start Of Functions #####################################################

# User Input into List

def modules():
    grade_list = []
    module_1 = grade_list.append(float(input("Please enter your grade for module 1: ")))
    module_2 = grade_list.append(float(input("Please enter your grade for module 2: ")))
    module_3 = grade_list.append(float(input("Please enter your grade for module 3: ")))
    module_4 = grade_list.append(float(input("Please enter your grade for module 4: ")))
    module_5 = grade_list.append(float(input("Please enter your grade for module 5: ")))
    module_6 = grade_list.append(float(input("Please enter your grade for module 6: ")))
    return grade_list
    
    

# Calculation of grades

def calc(grade_list):
    max_grade = max(grade_list)
    min_grade = min(grade_list)
    sum_grade = sum(grade_list)
    avg_grade = sum_grade / len(grade_list)
    avg_grade = Decimal(avg_grade)
    avg_grade = avg_grade.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    
    # Shows users the calculations
    print()
    print("--------------- Grade Calculations ---------------")
    print(f"{"Highest Grade":<20}:, {max_grade}%")
    print(f"{"Lowest Grade":<20}: {min_grade}%")
    print(f"{"Grade Sum":<20}: {sum_grade}")
    print(f"{"Grade Average":<20}: {avg_grade}%")
    print("--------------------------------------------------")
    print()
    
# Validates the choice of the user input 
    
def choice_valid(choice):
    while choice not in ["y", "n", "yes", "no"]:
        choice = input("Invalid input, please enter a y or n: ")
        choice = choice.lower()
    return choice
    
    
########################################### End Of Functions ##########################################


# Starts Main Loop so long as user does not enter "n" or "no"

def main():
    
    choice = 0

    # Runs first loop automatically
    
    while choice not in ["n", "no"]:
        grade_list = modules()
        calc(grade_list)

        # Allows user to choose to run another loop
        
        choice = input("Would you like to continue? (y/n): ")
        choice = choice_valid(choice)
        
        
    # When loop is exited, gives a goodbye statement
    print()
    print("*************************************************")
    print("Thank you for using my grade calculator😁😁😁😁")
    print("*************************************************")
    
main()