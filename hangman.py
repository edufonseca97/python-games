import random

def play():
    print_entrance()

    secret_word = random_word()
    # print(secret_word)

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

if(__name__ == "__main__"):
    play()