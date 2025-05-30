import random

def get_feedback():
    """
    Ask the user if the computer's guess was too high, too low, or correct.
    Returns one of: 'h', 'l', 'c'.
    """
    while True:
        feedback = input("Is my guess too High (h), too Low (l), or Correct (c)? ").lower()
        if feedback in ['h', 'l', 'c']:
            return feedback
        else:
            print("Please enter 'h' for high, 'l' for low, or 'c' for correct.")

def main():
    print("Think of a number between 1 and 100 and I'll try to guess it!")
    low = 1
    high = 100
    attempts = 0

    while True:
        if low > high:
            print("Hmm, seems like there's a contradiction in your answers. Let's try again!")
            break

        guess = random.randint(low, high)
        attempts += 1
        print(f"My guess is: {guess}")

        feedback = get_feedback()

        if feedback == 'c':
            print(f"Yay! I guessed your number {guess} in {attempts} tries.")
            break
        elif feedback == 'h':
            # Guess was too high, so adjust the high bound
            high = guess - 1
        elif feedback == 'l':
            # Guess was too low, so adjust the low bound
            low = guess + 1

if __name__ == "__main__":
    main()
