# Evan Westcott
# 20260317
# P4LAB1
# Building a house with the turtle library and loops

import turtle

# Create window popup
window = turtle.Screen()

# Background Color
window.bgcolor("beige")
# Create turtle drawing object that starts in the center of the screen
JEFF = turtle.Turtle()

# Jeff's Color("line color", "JEFF's fill color" )
JEFF.color("dark green", "red")


# Write a loop that executes 4 times to draw the square of the house
JEFF.begin_fill()
for side in range(4):
    
    #Draw one side of square
    JEFF.forward(200)
    JEFF.right(90)
JEFF.end_fill()

for top in range(3):
    JEFF.forward(200)
    JEFF.left(120)









# Keep window open until user closes
window.mainloop()