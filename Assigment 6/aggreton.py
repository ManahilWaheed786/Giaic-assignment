class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee

    def show_details(self):
        print(f"Department: {self.dept_name}")
        print(f"Employee: {self.employee.name}")


# Example usage
if __name__ == "__main__":
    emp = Employee("Alice")
    dept = Department("HR", emp)
    dept.show_details()
 