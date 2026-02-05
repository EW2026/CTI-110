# CTI-110
# Westcott, Evan
# 20260205
# Practice with Python and Team Instruction


# name = Bob

# Forced to enter first name
fname = input("Please enter your first name: ")
while fname == "":
    print("Please enter your first name ")
    fname = input("Please enter your first name: ")

# Forced to enter last name
lname = input("Please enter your last name: ")
while lname == "":
    print("Please enter last name ")
    lname = input("Please enter your last name: ")

hobby = input("what do you like to do for fun?: ")
while hobby == "":
    print("Please enter your hobby")
    hobby = input("what do you like to do for fun?: ")


# If first name and last name are entered, then print message
print() # Extra Blank Line
print(f"Nice to meet you {fname} {lname}!!!")
print(f"I'm glad you like to do {hobby}.")
print() # Extra Blank Line

# Introduction to for loops
print("I can repeat myself!")
count = input("How many times should I repeat myself?: ")
while count == "":
    print("please enter count")
    count = input("How many times should I repeat myself?: ")
# Valid in put was given
count = int(count)
for time in range(count):
    print("I know a song that drives people crazy,")