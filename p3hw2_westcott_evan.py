# Evan Westcott
# 20260304
# P3HW2
# Algorithm Tracks Pay Checks







#################### FUNCTIONS #######################

def ot(employee_hours, employee_pay, TIME_HALF):
    if employee_hours > 40:
        overtime = employee_hours - 40
        OVERTIME_PAY = employee_pay * TIME_HALF
        overtime_pay = OVERTIME_PAY * overtime
    else:
        overtime = 0
        overtime_pay = 0
    return overtime, overtime_pay
    


    
def GROSS_PAY(overtime, overtime_pay, time_half):
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
    days = int(input("How many holidays did you work?: "))
    for _ in range(days):
        print("For the question below, please enter all of the following that apply:")
        print("New Years Day, Martin Luther King Jr. Day, Presidents' Day, Memorial Day, Independence Day")
        print("Labor Day, Columbus Day, Veterans Day, Thanksgiving Day, Christmas Day")
        holiday = input("What holidays did you work?: ")
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
        HOLIDAY.append(holiday)   
    time_half = len(HOLIDAY) * holiday_hours
    time_half = time_half * TIME_HALF
    time_half = time_half * employee_pay
    return time_half 




def list_length(employee_name, employee_hours, employee_pay, overtime, overtime_pay, holiday_hours, time_half, gross_pay, EMPLOYEE_NAME, EMPLOYEE_INFO):
    # EMPLOYEE_NAME = {"name": employee_name, "pay": EMPLOYEE_INFO}
    #EMPLOYEE_INFO[EMPLOYEE_NAME] = {"Pay": employee_pay, "Hours": employee_hours, "O/T": overtime, "O/T Pay": overtime_pay, "Holiday Hours": holiday_hours, "Holiday PAY": time_half, "Gross Pay": gross_pay} 
    
    for _ in range(num_employees):
        EMPLOYEE_INFO[employee_name] = {"Pay": employee_pay, "Hours": employee_hours, "O/T": overtime, "O/T Pay": overtime_pay, "Holiday Hours": holiday_hours, "Holiday PAY": time_half, "Gross Pay": gross_pay} 
    return EMPLOYEE_INFO





# ################# Variables ##############


# Call everything
num_employees = int(input("Enter number of employees for current pay period: "))

TIME_HALF = 1.5
EMPLOYEE_NAME = {}
EMPLOYEE_INFO = {}

for _ in range(num_employees):
    employee_name = input("Enter employee name (Last, First): ")
    employee_hours = float(input("Enter Employee Hours: "))
    employee_pay = float(input("Enter Employee Pay: "))
    holiday_hours = float(input("How many hours did you work for the holiday(s) you worked?: "))
    
    
    overtime, overtime_pay = ot(employee_hours,employee_pay, TIME_HALF)
    
    time_half = time_and_half(employee_pay)
    
    print(time_half)
    
    gross_pay = GROSS_PAY(overtime, overtime_pay, time_half)
    
    # Call the function that populates the dictionary
    main_dict = list_length(employee_name, employee_hours, employee_pay, overtime, overtime_pay, holiday_hours, time_half, gross_pay, EMPLOYEE_NAME, EMPLOYEE_INFO)
    
    print(main_dict)