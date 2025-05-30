class Student:
    def __init__(self, name, marks):
        self.name = name        # Initialize name attribute
        self.marks = marks      # Initialize marks attribute

    def display(self):
        print("Student Details:")
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")


# Example usage
if __name__ == "__main__":
    # Create a Student object
    student1 = Student("Ali", 92)

    # Display student details
    student1.display()
