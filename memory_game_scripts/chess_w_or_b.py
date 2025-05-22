import random
import os
import time

def run_chess_color_guessing_game():
    columns = 'ABCDEFGH'
    rows = '12345678'

    while True:
        os.system('clear')  # Use 'cls' if you're on Windows, 'clear' for Unix/Linux

        random_column = random.choice(columns)
        random_row = random.choice(rows)
        square = f"{random_column}{random_row}"
        print(f"Random Chess Square: {square}")

        user_input = input("Guess the color of the square (w for white/b for black) or type 'exit' to stop: ")
        if user_input.lower() == 'exit':
            print("Exiting the game.")
            break

        # Determine the color of the square
        column_index = columns.index(random_column)
        row_index = rows.index(random_row)

        # If the sum of the indices is even, the square is black, otherwise, it is white
        if (column_index + row_index) % 2 == 0:
            correct_color = 'b'
        else:
            correct_color = 'w'

        if user_input.lower() == correct_color:
            print("Correct!")
        else:
            print(f"Incorrect! The correct color was {'white' if correct_color == 'w' else 'black'}.")
            time.sleep(3)

if __name__ == "__main__":
    run_chess_color_guessing_game()
