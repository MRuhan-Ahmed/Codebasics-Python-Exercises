"""
Exercise 17 - Inheritance
https://github.com/codebasics/py/tree/master/Basics/Exercise
"""


# 1. create inheritance using animal Dog relation.
# for example,
#     Animal and Dog both has same habitat
#     so create a method for habitat
#
# 2. use super() constructor for calling parent constructor.
# class Animal:
#     #code
#
# class Dog(Animal):
#     super()-it refers Animal class,
#     now you can call Animal's methods.

class Animal:
    """
    Represents a general animal with a specific habitat.

    :ivar habitat: str - The habitat where the animal lives.
    """

    def __init__(self, habitat: str) -> None:
        """
        Initialises the Animal class with a specified habitat.

        :param habitat: The habitat where the animal lives.
        """
        self.habitat = habitat

    def display_habitat(self) -> None:
        """Display the habitat of the animal."""
        print(f"1.\t{self.habitat}")


class Dog(Animal):
    """
    Represents a dog, which is a type of animal.

    Inherits from the Animal class and by default, initializes
    with the habitat 'Dog house'.

    :ivar habitat: The habitat of the dog (default is 'Dog house').
    """

    def __init__(self, habitat: str = "Dog house") -> None:
        """
        Initialise the dog with a specific habitat.

        :param habitat: The Dog house where the animal lives."""
        super().__init__(habitat)


def run_inheritance_example() -> None:
    """Runs the inheritance example with Dog and Animal classes."""
    dog1 = Dog()
    dog1.display_habitat()


if __name__ == "__main__":
    print(__doc__)
    run_inheritance_example()
