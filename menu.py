import hangman # Import the hangman game module
import number_guesser # Import the number guesser game module

def display_game_menu():
    """Display the game menu."""
    print("*********************")
    print("* Choose your game: *")
    print("*********************")
    print("(1) Hangman (2) Guess The Number")

def choose_game():
    """Get user input for game selection and execute the chosen game."""
    display_game_menu()

    while True:
        try:
            game_choice = int(input("Which Game? ")) # Get user's game choice
            if game_choice == 1:
                hangman.play() # Start the hangman game
                break
            elif game_choice == 2:
                number_guesser.play() # Start the number guesser game
                break
            else:
                print("Invalid option! Please enter a valid number.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

if(__name__ == "__main__"):
    choose_game() # Start the game selection process