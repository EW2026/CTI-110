"""
For loop loops through a collection of items
Collection could be a list or a dictionary, or make a list with the "range()" function
range(start, stop, step), start is inclusive, stop is exclusive    
"""
import time
# Write a loop that iterates(one loop) 4 times
total = 0

"""
for i in range(6):
    print(i)
    total = total + i
    print()
    print(f"current value of total {total}")
    time.sleep(3)
print(f"Total value of loop: {total}")
print()


for t in range(3,7):
    print(t)
    print()
print()
        

for s in range(0, 11, 2):
    print(s)
    print()
print()
"""


# Loop through a list

friends = ["Chelsea", "Debbie", "Timmy", "Andrew", "Hana"]

for friend in friends:
    print(friend)
    
    
# Loop Through Dictionary

cars = {"camaro": "red", "f-150": "white", "corolla": "silver"}

for k, v in cars.items():
    print(f" The {k} is {v}")
    
    
# Loop through dictionary keys only

for k in cars.keys():
    print(k)
    
    # Loop through dictionary values only

for v in cars.values():
    print(v)