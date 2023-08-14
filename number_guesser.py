import random

def play():
    print_entrance()

    lowest_number = 1
    highest_number = 100
    secret_number = random.randint(lowest_number, highest_number) # Generate a random number between 1 and 100
    attempts_left = 5 # Maximum attempts 

    while attempts_left > 0:
        try:
            guess = int(input(f"Guess the number (between {lowest_number} and {highest_number}): "))
            attempts_left -= 1

            if guess < secret_number:
                lowest_number = guess + 1 # Updated to show the lower limit
                print("Secret number is higher.")
            elif guess > secret_number:
                highest_number = guess - 1 # Upper limit updated
                print("Secret number is lower.")
            else:
                print("Congratulations! You have guessed the secret number! =D") # The game ends here if win
                break

            if attempts_left > 0:
                print(f"You have {attempts_left} {'attempt' if attempts_left == 1 else 'attempts'} left.\n")
            else:
                print(f"Sorry, you have run out of attempts. The secret number was {secret_number}.") # The game ends here if lose
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


def print_entrance():
    print("********************************");
    print("* Welcome to Guess the Number! *");
    print("********************************");

if(__name__ == "__main__"):
    play()