class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")


# Example usage
if __name__ == "__main__":
    obj1 = Counter()
    obj2 = Counter()
    obj3 = Counter()

    Counter.display_count()
