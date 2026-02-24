'''

# List Formatting

list_1 = ["bat", "cat", "hat", "green", "eggs", "ham"]

list_length = len(list_1)

print(list_1[2]) 


# list of numbers

list_2 = [1, 2, 3, 4, 5.5, 6, 7, 8, 9, 10]

# returns highest value

max_value = max(list_2)
print()
print(f"The maximum value in the list is: {max_value}")
print()

# returns lowest value

min_value = min(list_2)
print()
print(f"The minimum value in the list is: {min_value}")
print()

# returns sum of all values

sum_value = sum(list_2)
print()
print(f"The sum value of the list is: {sum_value}")
print()

# Hint: Average of a list = sum(list) / len(list)

'''

# Create empty list

user_list = []

# Gets  input from user to add to list

print()
list_input_1 = input("What do wish to put in the list?: ")
print()
list_input_2 = input("What do wish to put in the list?: ")
print()
list_input_3 = input("What do wish to put in the list?: ")
print()


# Adds the 3 items to the list through append

user_list.append(list_input_1)
user_list.append(list_input_2)
user_list.append(list_input_3)

# Prints List

print()
print(user_list)
print()