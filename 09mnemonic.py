import random
import os

# List of mnemonics
mnemonics = [
    (0, 'egg'),
    (1, 'candle'),
    (2, 'cobra'),
    (3, 'heart'),
    (4, 'flag'),
    (5, 'superman'),
    (6, 'cherry'),
    (7, 'axe'),
    (8, 'hourglass'),
    (9, 'racket')
]

def clear_screen():
    # Clear the screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

def practice_mnemonics():
    while True:
        # Select a random item from the list
        number, item = random.choice(mnemonics)
        
        # Display the item
        print(f"What number corresponds to: {item}?")
        
        # Get user input
        user_input = input("Enter the number: ")
        
        # Check if the input is correct
        if user_input.isdigit() and int(user_input) == number:
            print("Correct!")
        else:
            print(f"Wrong! The correct number is {number}.")
            input("Press Enter to continue...")
        
        # Clear the screen
        clear_screen()

# Start the practice
practice_mnemonics()
