import hangman

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
            game_choice = int(input("Which Game? "))
            if game_choice == 1:
                hangman.play()
                break
            elif game_choice == 2:
                print("*** Guess the number ***")
                # guessing.play()
                break
            else:
                print("Invalid option! Please enter a valid number.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

if(__name__ == "__main__"):
    choose_game()