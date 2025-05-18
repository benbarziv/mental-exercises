import random
import os

# List of mnemonics
mnemonics_months = [
    ("January", "New Years"),
    ("February", "Festival"),
    ("March", "Soldier"),
    ("April", "Shower"),
    ("May", "Flower"),
    ("June", "Beetle"),
    ("July", "Roman Empire"),
    ("August", "Me"),
    ("September", "School"),
    ("October", "Halloween"),
    ("November", "Facial Hair"),
    ("December", "Christmas")
]

mnemonics_images = [item[::-1] for item in mnemonics_months]

def clear_screen():
    # Clear the screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

def practice_mnemonics(category):
    if category == "months":
        mnemonics = mnemonics_months
    elif category == "images":
        mnemonics = mnemonics_images
    else:
        print("Invalid category")
        return
    
    while True:
        # Select a random item from the list
        name, item = random.choice(mnemonics)
        
        # Display the item
        print(f"What corresponds to: {item}?")
        
        # Get user input
        user_input = input("Enter the name: ")
        
        # Check if the input is correct
        if user_input.lower() == name.lower():
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is {name}.")
            input("Press Enter to continue...")
        
        # Clear the screen
        clear_screen()

# Start the practice
category = input("Choose category (months/images): ").strip().lower()
clear_screen()
practice_mnemonics(category)
