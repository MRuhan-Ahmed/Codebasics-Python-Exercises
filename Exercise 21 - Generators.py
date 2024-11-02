"""
Exercise 21 - Generators
https://github.com/codebasics/py/tree/master/Basics/Exercise
"""

from typing import Generator


# 1. Print Square Sequence using yield
#     Create Generator method such that every time it will return a next square number
#
# for example : 1 4 9 16 ...


def square_number(limit: int) -> Generator[int, None, None]:
    """
    Generates square numbers starting from 1 up to a specified limit.

    :param limit: The supremum for the generated square numbers.
    :yield: The next square number in the sequence.
    """
    a = 1
    while (square := a ** 2) <= limit:
        yield square
        a += 1


def main() -> None:
    """
    Prompts user for an upper limit and prints each square number up to that limit.
    """
    try:
        limit = int(input("\tEnter an upper limit for the square sequence: "))
        if limit <= 0:
            raise ValueError("The limit must be a positive integer.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    print(f"\tSquare sequence up to {limit}:")
    for square in square_number(limit):
        print(f"\t{square}")


if __name__ == "__main__":
    print(__doc__)
    main()
