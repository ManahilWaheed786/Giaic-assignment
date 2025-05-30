class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def display(self):
        print(f"Name: {self.name}")
        print(f"Subject: {self.subject}")


# Example usage
if __name__ == "__main__":
    teacher = Teacher("Mr. Ahmed", "Mathematics")
    teacher.display()
