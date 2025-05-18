import random
import os
import time

def generate_squares():
    """Generate two random chess board squares."""
    columns = 'ABCDEFGH'
    rows = '123456789'
    square1 = random.choice(columns) + random.choice(rows)
    square2 = random.choice(columns) + random.choice(rows)
    return square1, square2

def get_in_between_columns(square1, square2):
    """Get the columns between two squares."""
    col1, col2 = sorted([square1[0], square2[0]])
    if ord(col2) - ord(col1) == 1:
        return 'n'  # Adjacent columns
    elif ord(col2) - ord(col1) > 1:
        return ''.join(chr(c) for c in range(ord(col1) + 1, ord(col2)))
    else:
        return 'n'  # Same or no columns in between

def chess_blindfold_game():
    print("Welcome to the blindfold chess training game!")
    while True:
        os.system('clear')
        square1, square2 = generate_squares()
        print(f"The two random squares are: {square1}, {square2}")
        answer = input("Please enter the columns in between or type 'exit' to exit: ")
        if answer.lower() == 'exit':
            print("Exiting game. Thank you for playing!")
            break
        correct_answer = get_in_between_columns(square1, square2)
        if answer.lower() == correct_answer.lower():
            print("Correct!")
        else:
            print(f"The correct answer was: {correct_answer}")
        time.sleep(1)

# Call the function to start the game
chess_blindfold_game()
