def choose_game():
    print("*********************************")
    print("********Choose your game:********")
    print("*********************************")

    print("(1) Hangman (2) Guessing")

    game = int(input("Which Game? "))

    if(game == 1):
        print("*** HANGMAN ***")
        # hangman.play()
    elif(game == 2):
        print("*** GUESSING ***")
        # guessing.play()
    else:
        print("Invalid option! Pick another one.")

if(__name__ == "__main__"):
    choose_game()