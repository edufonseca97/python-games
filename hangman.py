import random

def play():
    print_entrance()

    secret_word = random_word()
    print(secret_word)

    right_letters = secret_letters(secret_word)
    print(right_letters)

    finish = False
    errors = 0

    while(not finish and errors < 7):

        guess = player_guess()

        if(guess in secret_word):
            # change right letters
            print(guess)
        else:
            errors += 1

        finish = "_" not in right_letters

        print(right_letters)

    if(finish):
        print("Congratulations!")
    else:
        print("You lost!")

def print_entrance():
    print("***********************");
    print("* Welcome to Hangman! *");
    print("***********************");

def random_word():
    file = open("wordbank.txt", "r")
    words = []

    for line in file:
        line = line.strip()
        words.append(line)

    file.close()

    number = random.randrange(0, len(words))
    secret_word = words[number].upper()
    return secret_word

def secret_letters(word):
    return ["_" for letter in word]

def player_guess():
    guess = input("Guess a letter: ")
    guess = guess.strip().upper()
    return guess

if(__name__ == "__main__"):
    play()