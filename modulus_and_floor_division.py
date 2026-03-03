# modulus symbol is "%"print"
# only gives the remainder

# Floor Division symbol "//"
# Gives the lower whole number

num = 18
divisor = 5
remaining = num % divisor


if num % divisor == 0:
    print(f"{num} is divisible by {divisor}")
    
else:
    print(f"{num} divided by {divisor} remaining amount is {remaining}")