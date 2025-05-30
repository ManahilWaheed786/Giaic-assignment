import time

def countdown(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")  # Overwrites the line in the console
        time.sleep(1)
        seconds -= 1
    print("Time's up!            ")

def main():
    total_seconds = int(input("Enter the time in seconds for the countdown: "))
    print("Starting countdown...")
    countdown(total_seconds)

if __name__ == "__main__":
    main()
