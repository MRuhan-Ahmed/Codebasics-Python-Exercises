"""
Exercise 16 - Classes & Objects
https://github.com/codebasics/py/tree/master/Basics/Exercise
"""


# 1. Create a sample class named Employee with two attributes id
# and name employee :
#     id
#     name
# object initializes id and name dynamically
# for every Employee object created.
# emp = Employee(1, "coder")

class Employee:
    """
    Represents an employee with a unique ID and a name.

    :param employee_id: The unique identifier for the employee.
    :param employee_name: The name of the employee.
    """

    def __init__(self,
                 employee_id: int,
                 employee_name: str) -> None:
        self.id = employee_id
        self.name = employee_name

    def display(self) -> None:
        """Displays the employee's ID and name."""
        print(f"1.\tID: {self.id}\tName: {self.name}")

    def delete_id(self) -> None:
        """Deletes the employee's ID."""
        del self.id


def question1(emp: Employee) -> None:
    """Executes the employee creation process."""
    emp.display()

# 2. Use del property to first delete id attribute
# and then the entire object.


def question2(emp: Employee) -> None:
    """Executes the employee deletion process."""

    # Delete the id attribute
    emp.delete_id()
    try:
        emp.display()   # This will raise an error since id is deleted
    except AttributeError:
        print("2.\tID attribute has been deleted and cannot be accessed.")

    # Delete the entire object
    del emp
    try:
        emp.display()   # This will raise an error since emp no longer exists
    except NameError:
        print("2.\tThe employee object no longer exists.")


def main() -> None:
    """Executes all question functions sequentially."""
    employee1 = Employee(1, "coder")
    question1(employee1)
    question2(employee1)


if __name__ == "__main__":
    print(__doc__)
    main()
