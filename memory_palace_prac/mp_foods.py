import random
import os

# Lists of mnemonics
mnemonics_countries = [
    ("Argentina", "Asado"),
    ("Australia", "Meat Pie"),
    ("Bangladesh", "Panta Bhat"),
    ("Bhutan", "Ema Datshi"),
    ("Brazil", "Feijoda"),
    ("Cambodia", "Amok Trey"),
    ("Canada", "Butter Tart"),
    ("Canada", "Putine"),
    ("Chile", "Empenada"),
    ("China", "Dim Sum"),
    ("China", "Pecking Duck"),
    ("Columbia", "Arepa"),
    ("Cuba", "Ropa Veijea"),
    ("Dominican Republic", "Sancocho"),
    ("Ecuador", "Ceviche"),
    ("Egypt", "Koshari"),
    ("Ethiopia", "Doro Wat"),
    ("Fiji", "Kokoda"),
    ("France", "Coc a Vin"),
    ("France", "Ratatoullie"),
    ("Germany", "Sourbratten"),
    ("Greece", "Moussaka"),
    ("Haiti", "Griot"),
    ("India", "Biryani"),
    ("India", "Masala Dosa"),
    ("Indonesia", "Rendang"),
    ("Iran", "Fesengan"),
    ("Israel", "Humus"),
    ("Italy", "Rissoto"),
    ("Italy", "Tiramisu"),
    ("Jamaica", "Jerk Chicken"),
    ("Japan", "Ramen"),
    ("Japan", "Sushi"),
    ("Korea", "Bulgogi"),
    ("Korea", "Kimchi"),
    ("Lebanon", "Tabule"),
    ("Malaysia", "Laksa"),
    ("Mexico", "Mole"),
    ("Mexico", "Tacos"),
    ("Mongolia", "Korckhog"),
    ("Morocco", "Tagine"),
    ("Nepal", "Momo"),
    ("Netherlands", "Stroopwaffel"),
    ("New Zealand", "Hangi"),
    ("Pakistan", "Nihari"),
    ("Peru", "Sancocho Gallari"),
    ("Philippines", "Adobo"),
    ("Portugal", "Bacalhau au Bras"),
    ("Russia", "Borsht"),
    ("Saudi Arabia", "Kabsa"),
    ("Spain", "Gazpacho"),
    ("Spain", "Paella"),
    ("Sri Lanka", "Fish Ambule Thiyal"),
    ("Thailand", "Pad Thai"),
    ("Trinidad and Tobago", "Doubles"),
    ("Turkey", "Kabab"),
    ("UK", "Fish and Chips"),
    ("USA", "BBQ Ribs"),
    ("USA", "Clam Chowder"),
    ("USA", "Jambalaya"),
    ("Venezuela", "Pabellon Criollo"),
    ("Vietnam", "Pho")
]

mnemonics_food = [item[::-1] for item in mnemonics_countries]

def clear_screen():
    # Clear the screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

def practice_mnemonics(category):
    if category == "countries":
        mnemonics = mnemonics_countries
    elif category == "food":
        mnemonics = mnemonics_food
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
category = input("Choose category (countries/food): ").strip().lower()
clear_screen()
practice_mnemonics(category)
