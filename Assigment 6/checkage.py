class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")
    else:
        print("Age is valid.")

# Example usage
if __name__ == "__main__":
    try:
        check_age(16)
    except InvalidAgeError as e:
        print(f"Error: {e}")
