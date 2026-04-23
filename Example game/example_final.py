# beginner file for final project
# assuming text based game in terminal
# Pip install Tkinter
# Pip install TkGifWidget

import random as ran
import tkinter as tk


def JEFF():
    name = "Jeff" # can allow user input
    health = 100  # can allow user input
    inventory = ["🍓","🍓"] # Strawberry gives hp
    
    # Create a dictionary to represent the character
    character = {"name":name, "HP":health, "inv":inventory}
    
    return character
    
def show_stats(character):
    print()
    for k, v in character.items():
        print(f"{k}: {v}")
    print()


# Shows Gif in a pop-up window




def main():
    print("Your journey awaits")
    
    # Call the function that creates the main character
    mc = JEFF()
    # Call function to show character stats; pass main call of
    # mc since the show_stats depends on the mc variable
    show_stats(mc)
    
    # Code 1/3 chance that character gets attacked by a bear
    print("An aggressive bear is coming torward you")
    attack_chance = ran.choice([1, 2, 3])
    if attack_chance == 1:
        print("You are unlucky today, and could not scuttle away🩸")
        
        # Get health value from dictionary to decrease it
        damage = ran.randint(1, 15)
        mc["HP"] -= damage
        print(f"You took {damage} damage.")
        show_stats(mc)
    else:
        print("Your little legs moved fast today and were able to scuttle away 👌")
    
if __name__ == "__main__":
    main()
    