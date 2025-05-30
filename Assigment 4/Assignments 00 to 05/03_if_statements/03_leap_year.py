def main():
    # Get the year to check from the user
    year = int(input('Please input a year: '))

    if year % 4 == 0:  # Check divisibility by 4
        if year % 100 == 0:  # Check divisibility by 100
            if year % 400 == 0:  # Check divisibility by 400
                print("That's a leap year!")
            else:
                print("That's not a leap year.")
        else:
            print("That's a leap year!")
    else:
        print("That's not a leap year.")

if __name__ == '__main__':
    main()
