def double(num: int):
    return num * 2

def main():
    num = int(input("Enter a number: "))
    num_times_2 = double(num)
    print("Double that is", num_times_2)

# Required line to call the main function
if __name__ == '__main__':
    main()
