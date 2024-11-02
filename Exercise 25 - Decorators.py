"""
Exercise 25 - Decorators
https://github.com/codebasics/py/tree/master/Basics/Exercise
"""

# 1. Create a decorator function to check that the argument
# passed to the function factorial is a non-negative integer:
#
# 2. Create a factorial function which finds the factorial of a number.
#
# 3. Use the decorator to decorate the factorial function
# to only allow factorial of non-negative integers.

from typing import Callable


def factorial_check(function: Callable[[int], int]) -> Callable[[int], int]:
    """
    A decorator that checks if the argument passed to the decorated function is a non-negative integer.

    :param function: The function to decorate.
    :return: The wrapped function which raises an exception if the input is invalid.
    """
    def wrapper(number: int) -> int:
        """
        Checks if the input number is a non-negative integer before calling the decorated function.

        :param number: The integer to check and then pass to the decorated function.
        :raises ValueError: If the number is not a non-negative integer.
        :return: The result of the decorated function if input is valid.
        """
        if not isinstance(number, int) or number < 0:
            raise ValueError("Your input is not a non-negative integer")

        return function(number)

    return wrapper


@factorial_check
def factorial(number: int) -> int:
    """
    Calculates the factorial of a given non-negative integer.

    :param number: A non-negative integer whose factorial is to be calculated.
    :return: The factorial of the number.
    """
    if number == 0:
        return 1
    return number * factorial(number - 1)


def question1() -> None:
    """
    Demonstrates the factorial decorator by validating if a number is non-negative.
    Shows an error if a negative integer is passed.
    """
    try:
        print(f"1.\tAttempting to calculate factorial of -1 (expecting error):"
              f"\t{factorial(-1)}")
    except ValueError as e:
        print(f"\tError: {e}")


def question2() -> None:
    """
    Calculates and prints factorials of numbers from 0 to 9 using the factorial function.
    """
    print("2.\tCalculating factorials for numbers from 0 to 9:")
    for integer in range(10):
        print(f"\t{integer}! = {factorial(integer)}")


def main() -> None:
    """Executes all question functions sequentially."""
    question1()
    question2()


if __name__ == "__main__":
    print(__doc__)
    main()
