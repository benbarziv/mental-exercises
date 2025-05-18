import random
import os
import time

def run_chess_piece_placement_game():
    # Correct mapping of pieces to their starting positions with accurate notation
    piece_positions = {
        'b-K-w': ['E8'], 'b-Q-b': ['D8'], 'b-B-w': ['C8'], 'b-B-b': ['F8'],
        'b-N-w': ['G8'], 'b-N-b': ['B8'], 'b-R-w': ['A8'], 'b-R-b': [ 'H8'],
        'b-P': ['7'], 'w-K-b': ['E1'], 'w-Q-w': ['D1'], 'w-B-b': ['C1'],'w-B-w': ['F1'], 'w-N-b': [ 'G1'],
        'w-N-w': ['B1'], 'w-R-b': ['A1'], 'w-R-w': ['H1'],
        'w-P': ['2']
    }

    pieces = list(piece_positions.keys())
    streak = 0
    while True:
        os.system('clear')  # Use 'cls' if you're on Windows, 'clear' for Unix/Linux
        print(f"current streak: {streak} \n")
        random_piece = random.choice(pieces)
        print(f"Random Piece: {random_piece}")

        user_input = input("Guess the starting square(s) or type 'exit' to stop: ")
        if user_input.lower() == 'exit':
            print("Exiting the game.")
            break

        correct_squares = piece_positions[random_piece]

        # Check if user input is correct
        if user_input.upper() in correct_squares or user_input == correct_squares[0]:
            print("Correct!")
            streak +=1
        else:
            print(f"Incorrect! The correct answer was {' or '.join(correct_squares)}.")
            time.sleep(3)
            streak = 0

if __name__ == "__main__":
    run_chess_piece_placement_game()