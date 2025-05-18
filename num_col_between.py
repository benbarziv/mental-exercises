import random
import os
import time

def run_letter_difference_game():
    letters = 'ABCDEFGH'

    while True:
        os.system('clear')  # Use 'cls' if you're on Windows, 'clear' for Unix/Linux
        random_letter1 = random.choice(letters)
        random_letter2 = random.choice(letters)
        print(f"Random Letters: {random_letter1}, {random_letter2}")

        user_input = input("Guess the number of columns between or type 'exit' to stop: ")
        if user_input.lower() == 'exit':
            print("Exiting the game.")
            break

        letter_value1 = letters.index(random_letter1)
        letter_value2 = letters.index(random_letter2)

        # Calculate the difference by explicitly subtracting the smaller from the larger
        start = min(letter_value1, letter_value2) + 1
        end = max(letter_value1, letter_value2)
        columns_between = letters[start:end]  # This gets the letters between the two chosen letters
        difference_of_values = end - start

        if user_input.isdigit() and int(user_input) == difference_of_values:
            print(f"Correct! Columns between were {', '.join(columns_between)}.")
        else:
            print(f"Incorrect! The correct number of columns was {difference_of_values}. Columns between were {', '.join(columns_between)}.")

        time.sleep(2)  # Delay to allow the user to see the correct answer

if __name__ == "__main__":
    run_letter_difference_game()
