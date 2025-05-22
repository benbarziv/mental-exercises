import random
import os
import time

def run_chess_piece_guessing_game():
    columns = 'ABCDEFGH'
    # Use weighted choices for rows to reduce pawn frequency
    rows = ['1', '8'] * 3 + ['2', '7']  # Increase the weight of rows 1 and 8

    # Mapping of columns to their initial pieces
    piece_mapping = {
        'A': 'R', 'B': 'N', 'C': 'B', 'D': 'Q', 'E': 'K', 'F': 'B', 'G': 'N', 'H': 'R',
        '1': 'R', '2': 'P', '7': 'P', '8': 'R'
    }

    while True:
        os.system('clear')  # Use 'cls' if you're on Windows, 'clear' for Unix/Linux

        random_column = random.choice(columns)
        random_row = random.choice(rows)
        square = f"{random_column}{random_row}"
        print(f"Random Square: {square}")

        user_input = input("Guess the piece on the square (P, R, N, B, Q, K) or type 'exit' to stop: ")
        if user_input.lower() == 'exit':
            print("Exiting the game.")
            break

        # Determine the piece on the square
        if random_row in '18':
            correct_piece = piece_mapping[random_column]
        elif random_row in '27':
            correct_piece = piece_mapping[random_row]

        if user_input.upper() == correct_piece:
            print("Correct!")
        else:
            print(f"Incorrect! The correct piece was {correct_piece}.")
            time.sleep(3)

if __name__ == "__main__":
    run_chess_piece_guessing_game()

