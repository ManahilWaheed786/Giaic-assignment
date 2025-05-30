class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public
        self._salary = salary     # Protected
        self.__ssn = ssn          # Private

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")


# Example usage
if __name__ == "__main__":
    emp = Employee("Ali", 50000, "123-45-6789")

    # Accessing public variable
    print("Accessing public:", emp.name)

    # Accessing protected variable
    print("Accessing protected:", emp._salary)

    # Trying to access private variable directly (will raise AttributeError)
    try:
        print("Accessing private:", emp.__ssn)
    except AttributeError as e:
        print("Accessing private:", e)

    # Accessing private variable using name mangling
    print("Accessing private with name mangling:", emp._Employee__ssn)
