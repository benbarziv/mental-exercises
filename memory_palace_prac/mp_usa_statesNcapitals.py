import random
import os

# List of mnemonics with corrected spellings
mnemonics_states = [
    ("Alabama", "Montgomery"),
    ("Alaska", "Juneau"),
    ("Arizona", "Phoenix"),
    ("Arkansas", "Little Rock"),
    ("California", "Sacramento"),
    ("Colorado", "Denver"),
    ("Connecticut", "Hartford"),
    ("Delaware", "Dover"),
    ("Florida", "Tallahassee"),
    ("Georgia", "Atlanta"),
    ("Hawaii", "Honolulu"),
    ("Idaho", "Boise"),
    ("Illinois", "Springfield"),
    ("Indiana", "Indianapolis"),
    ("Iowa", "Des Moines"),
    ("Kansas", "Topeka"),
    ("Kentucky", "Frankfort"),
    ("Louisiana", "Baton Rouge"),
    ("Maine", "Augusta"),
    ("Maryland", "Annapolis"),
    ("Massachusetts", "Boston"),
    ("Michigan", "Lansing"),
    ("Minnesota", "St. Paul"),
    ("Mississippi", "Jackson"),
    ("Missouri", "Jefferson City"),
    ("Montana", "Helena"),
    ("Nebraska", "Lincoln"),
    ("Nevada", "Carson City"),
    ("New Hampshire", "Concord"),
    ("New Jersey", "Trenton"),
    ("New Mexico", "Santa Fe"),
    ("New York", "Albany"),
    ("North Carolina", "Raleigh"),
    ("North Dakota", "Bismarck"),
    ("Ohio", "Columbus"),
    ("Oklahoma", "Oklahoma City"),
    ("Oregon", "Salem"),
    ("Pennsylvania", "Harrisburg"),
    ("Rhode Island", "Providence"),
    ("South Carolina", "Columbia"),
    ("South Dakota", "Pierre"),
    ("Tennessee", "Nashville"),
    ("Texas", "Austin"),
    ("Utah", "Salt Lake City"),
    ("Vermont", "Montpelier"),
    ("Virginia", "Richmond"),
    ("Washington", "Olympia"),
    ("West Virginia", "Charleston"),
    ("Wisconsin", "Madison"),
    ("Wyoming", "Cheyenne")
]

mnemonics_capitals = [item[::-1] for item in mnemonics_states]

def clear_screen():
    # Clear the screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

def practice_mnemonics(category):
    if category == "states":
        mnemonics = mnemonics_states
    elif category == "capitals":
        mnemonics = mnemonics_capitals
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
category = input("Choose category (states/capitals): ").strip().lower()
clear_screen()
practice_mnemonics(category)
