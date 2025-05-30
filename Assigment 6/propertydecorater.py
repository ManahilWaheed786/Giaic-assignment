class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            print("Invalid price. Must be non-negative.")

    @price.deleter
    def price(self):
        del self._price


# Example usage
if __name__ == "__main__":
    p = Product(100)
    print(p.price)       # Get price
    p.price = 150        # Set new price
    print(p.price)
    del p.price          # Delete price
