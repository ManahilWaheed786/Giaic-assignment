import random

def get_user_guess():
    """Prompt the user to enter a guess and return it as an integer."""
    while True:
        guess = input("Enter your guess (between 1 and 100): ")
        if guess.isdigit():
            guess = int(guess)
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        else:
            print("That's not a valid number. Try again.")

def main():
    print("Welcome to Guess the Number!")
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed = False

    while not guessed:
        guess = get_user_guess()
        attempts += 1

        if guess < secret_number:
            print("Your guess is too low, try again.")
        elif guess > secret_number:
            print("Your guess is too high, try again.")
        else:
            print(f"Congrats! You guessed it in {attempts} attempts!")
            guessed = True

if __name__ == "__main__":
    main()

