import random

def main():
    # Generate the secret number at random!
    secret_number = random.randint(0, 99)
    
    print("I am thinking of a number between 0 and 99...")
    
    # Get user's guess
    guess = int(input("Enter a guess: "))
    # Loop until guess equals secret number
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
            
        print()  # Empty line for readability
        guess = int(input("Enter a new number: "))
        
    print("Congrats! The number was: " + str(secret_number))

if __name__ == '__main__':
    main()
