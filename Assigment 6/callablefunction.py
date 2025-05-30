class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor


# Example usage
if __name__ == "__main__":
    multiply_by_3 = Multiplier(3)
    
    print(callable(multiply_by_3))  # True, because __call__ is defined
    print(multiply_by_3(10))        # 30
    print(multiply_by_3(7))         # 21
