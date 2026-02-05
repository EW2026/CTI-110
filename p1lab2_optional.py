# CTI-110
# Westcott, Evan
# 20260205
# Practice with Python and Team Instruction


# name = Bob

# Forced to enter first name
fname = input("Please enter your first name: ")

while fname == "":
    print("Please enter your first name ")
    fname = input("Please enter your first name ")
lname = input("Please enter your last name ")

# Forced to enter last name
while lname == "":
    print("Please enter your last name")
    fname = input("Please enter your last name ")

hobby = input("what do you like to do for fun? ")
while hobby == "":
    print("Please enter your hobby")
    hobby = input("what do you like to do for fun? ")


# If first name and last name are entered, then print message
print() # Extra Blank Line
print(f"Nice to meet you {fname} {lname}!!!")
print(f"I'm glad you like to do {hobby}.")
print() # Extra Blank Line

# Introduction to for loops
print("I can repeat myself!")
count = int(input("How many times should I repeat myself? "))
while count == "":
    print("please enter count")
    count = int(input("How many times should I repeat myself? "))
for time in range(count):
    print("I know a song that drives people crazy,")