import random
import os
import time

def run_letter_sum_game():
    letters = 'ABCDEFGH'

    while True:
        os.system('clear')  # Use 'cls' if you're on Windows, 'clear' for Unix/Linux
        random_letter1 = random.choice(letters)
        random_letter2 = random.choice(letters)
        print(f"Random Letters: {random_letter1}, {random_letter2}")

        user_input = input("Guess the sum of the letters or type 'exit' to stop: ")
        if user_input.lower() == 'exit':
            print("Exiting the game.")
            break

        letter_value1 = letters.index(random_letter1) + 1
        letter_value2 = letters.index(random_letter2) + 1
        sum_of_values = letter_value1 + letter_value2

        if user_input.isdigit() and int(user_input) == sum_of_values:
            print("Correct!")
            continue  # Immediately restart the loop, skipping the delay
        else:
            print(f"Incorrect! The correct sum was {sum_of_values}.")
            time.sleep(3)  # Delay to allow the user to see the correct answer

if __name__ == "__main__":
    run_letter_sum_game()
