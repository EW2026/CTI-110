# Evan Westcott
# 20260304
# P3HW2
# Algorithm Tracks Pay Checks

################# Class #################

def ot(employee_hours, employee_pay, TIME_HALF):
    if employee_hours > 40:
        overtime = employee_hours - 40
        overtime_pay = employee_pay * TIME_HALF
    else:
        overtime = 0
        overtime_pay = 0
    return overtime, overtime_pay 
    
def gross_pay(overtime, overtime_pay, time_half):
    gross_pay = employee_hours * employee_pay
    
    if employee_hours <= 40:
        gross_pay = gross_pay
        return gross_pay

    elif time_half > 0 and overtime > 0:
        gross_pay = gross_pay + time_half + overtime_pay

    elif time_half >0:
        gross_pay = gross_pay + time_half
    
    else:   
        gross_pay = overtime * overtime_pay + gross_pay
    return gross_pay

def time_and_half(employee_pay):
    HOLIDAY = []
    days= []
    days = int(input("How many holidays did you work?: "))
    for _ in range(days):
        print("For the question below, please enter all of the following that apply:")
        print("New Years Day, Martin Luther King Jr. Day, Presidents' Day, Memorial Day, Independence Day")
        print("Labor Day, Columbus Day, Veterans Day, Thanksgiving Day, Christmas Day")
        holiday = holiday(input("What holidays did you work?: "))
        while holiday not in ["New Years Day",
                           "Martin Luther King Jr. Day",
                            "Presidents' Day",
                            "Memorial Day", 
                            "Independence Day",
                            "Labor Day",
                            "Columbus Day",
                            "Veterans Day",
                            "Thanksgiving Day",
                            "Christmas Day"]:
            holiday = input("invalid entry(s), please enter the holidays as listed above")
        holiday = HOLIDAY.append(holiday)   
        time_half = len(HOLIDAY) * holiday_hours
        time_half = time_half * TIME_HALF
        time_half = time_half * employee_pay
    return time_half 

def list_length(employee_name, employee_hours, employee_pay):
    employee_list = {employee_name: {}}
    for _ in range(num_employees):
        employee_hours
        employee_pay



    ################# Variables ##############


num_employees = int(input("Enter number of employees for current pay period: "))
employee_name = input("Enter employee name (Last, First): ")
employee_hours = float(input("Enter Employee Hours: "))
employee_pay = float(input("Enter Employee Pay: "))
holiday_hours = float(input("How many hours did you work for the holiday(s) you worked?: "))

TIME_HALF = 1.5
