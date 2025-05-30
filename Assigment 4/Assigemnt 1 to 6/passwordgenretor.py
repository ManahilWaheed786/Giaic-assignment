import random
import string

def generate_password(length):
    # Combine letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly pick characters for the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    num_passwords = int(input("How many passwords would you like to generate? "))
    length = int(input("Enter the length for each password: "))

    print("\nGenerated passwords:")
    for _ in range(num_passwords):
        print(generate_password(length))

if __name__ == "__main__":
    main()
