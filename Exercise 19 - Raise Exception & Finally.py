"""
Exercise 19 - Raise Exception & Finally
https://github.com/codebasics/py/tree/master/Basics/Exercise
"""


# 1. Create a custom exception AdultException.
#
# 2. Create a class Person with attributes name and age in it.
#
# 3. Create a function get_minor_age() in the class.
# It throws an exception if the person is adult otherwise returns age.
#
# 4. Create a function display_person() which prints the age and name of a person.
#
# let us say,
#
# if age>18
#     he is major
# else
#     raise exception
#
# create customException named is_major and raise it if age < 18.


class AdultException(Exception):
    """Custom exception raised when the age indicates an adult."""

    def __init__(self, message: str) -> None:
        """
        Initializes the AdultException with a message.

        :param message: Message to display when the exception is raised.
        """
        super().__init__(message)

    def __str__(self) -> str:
        """
        Returns the exception message for printing or logging.

        :return: A string representation of the exception message.
        """
        return f"AdultException: {self.args[0]}"


class Person:
    """Class representing a person with a name and age."""

    def __init__(self, name: str, age: int) -> None:
        """
        Initializes a Person instance.

        :param name: The name of the person.
        :param age: The age of the person.
        """
        self.name = name
        self.age = age

    def get_minor_age(self) -> int:
        """
        Checks if the person is a minor (age <= 18).
        If the person is an adult, raises AdultException.

        :raises AdultException: If the person is an adult (age > 18).
        :return: The age of the person if they are a minor.
        """
        if self.age > 18:
            raise AdultException("Person is an adult")
        return self.age

    def display_person(self) -> None:
        """
        Displays the person's name and age if they are a minor.
        Catches AdultException if the person is an adult and outputs a relevant message.
        """
        try:
            age = self.get_minor_age()
            print(f"\tAge: {age}")
        except AdultException as error:
            print(f"\t{error}")
        finally:
            print(f"\tName: {self.name}")


def main() -> None:
    """Create a person instance and display information"""
    try:
        person = Person("ABD", 19)
        person.display_person()
    except ValueError as e:
        print(f"Invalid input encountered: {e}")


if __name__ == "__main__":
    print(__doc__)
    main()
