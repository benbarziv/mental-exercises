import random
import os

# List of mnemonics
mnemonics_books = [
    ("Albert Camus", "The Stranger"),
    ("Aldous Huxley", "A Brave New World"),
    ("Alice Walker", "The Color Purple"),
    ("Charles Dickens", "The Tale of Two Cities"),
    ("Charlotte Bronte", "Jane Eyre"),
    ("Chinua Achebe", "Things Fall Apart"),
    ("Dante Alighieri", "The Divine Comedy"),
    ("Edgar Allan Poe", "The Raven"),
    ("Emily Dickinson", "Because I could not stop for death"),
    ("Ernest Hemingway", "The Old Man and The Sea"),
    ("F. Scott Fitzgerald", "The Great Gatsby"),
    ("Gabriel Garcia Marquez", "One Hundred Years of Solitude"),
    ("George Orwell", "1984"),
    ("Harper Lee", "To Kill a Mockingbird"),
    ("Herman Melville", "Moby Dick"),
    ("J.D. Salinger", "The Catcher in the Rye"),
    ("Jane Austen", "Pride and Prejudice"),
    ("James Joyce", "Ulysses"),
    ("J.K. Rowling", "Harry Potter and The Philosopher's Stone"),
    ("John Steinbeck", "The Grapes of Wrath"),
    ("Joseph Conrad", "Heart of Darkness"),
    ("Jorge Luis Borges", "Ficciones"),
    ("Leo Tolstoy", "War and Peace"),
    ("Louisa May Alcott", "Little Women"),
    ("Marcel Proust", "In Search of Lost Time"),
    ("Mark Twain", "The Adventures of Huckleberry Finn"),
    ("Mary Shelley", "Frankenstein"),
    ("Miguel de Cervantes", "Don Quixote"),
    ("Nathaniel Hawthorne", "The Scarlet Letter"),
    ("Oscar Wilde", "The Picture of Dorian Gray"),
    ("Ralph Ellison", "Invisible Man"),
    ("Ray Bradbury", "Fahrenheit 451"),
    ("Salman Rushdie", "Midnight's Children"),
    ("Sylvia Plath", "The Bell Jar"),
    ("Tennessee Williams", "A Streetcar Named Desire"),
    ("Toni Morrison", "Beloved"),
    ("Victor Hugo", "Les Miserables"),
    ("Virginia Woolf", "Mrs Dalloway"),
    ("Vladimir Nabokov", "Lolita"),
    ("William Faulkner", "The Sound and the Fury"),
    ("William Shakespeare", "Hamlet"),
    ("Zora Neale Hurston", "Their Eyes Were Watching God")
]

mnemonics_authors = [item[::-1] for item in mnemonics_books]

def clear_screen():
    # Clear the screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

def practice_mnemonics(category):
    if category == "books":
        mnemonics = mnemonics_books
    elif category == "authors":
        mnemonics = mnemonics_authors
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
category = input("Choose category (books/authors): ").strip().lower()
clear_screen()
practice_mnemonics(category)
