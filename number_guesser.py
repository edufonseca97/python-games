import random

def play():
    print_entrance()

    secret_number = random.randint(1, 100) # Generate a random number between 1 and 100
    max_attempts = 5
    player_attempts = 0    

    while player_attempts < max_attempts:
        try:
            guess = int(input("Guess the number (between 1 and 100): "))
            player_attempts += 1

            if guess < secret_number:
                print("Secret number is higher.")
            elif guess > secret_number:
                print("Secret number is lower.")
            else:
                print("Congratulations! You have guessed the secret number! =D")
                break

            remaining_attempts = max_attempts - player_attempts
            if remaining_attempts > 0:
                print(f"You have {remaining_attempts} {'attempt' if remaining_attempts == 1 else 'attempts'} left.\n")
            else:
                print(f"Sorry, you have run out of attempts. The secret number was {secret_number}.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


def print_entrance():
    print("********************************");
    print("* Welcome to Guess the Number! *");
    print("********************************");

if(__name__ == "__main__"):
    play()