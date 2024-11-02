"""
Exercise 26 - Multithreading
https://github.com/codebasics/py/tree/master/Basics/Exercise
"""

# 1. Create any multithreaded code using for loop for creating multi-threads
# for i in range(10):
#     th = Thread(target=func_name, args=(i, ))

import threading


def calculate_square(numbers: list[int]) -> None:
    """
    Prints the square of each number in the provided list.

    :param numbers: A list of integers to square.
    """
    print("\n\tSquare numbers:")

    for number in numbers:
        print(f"\t{number}² = {number ** 2}")


def calculate_cube(numbers: list[int]) -> None:
    """
    Prints the cube of each number in the provided list.

    :param numbers: A list of integers to cube.
    """
    print("\n\tCube numbers:")

    for number in numbers:
        print(f"\t{number}³ = {number ** 3}")


def main() -> None:
    """
    Asks the user to enter a list of non-negative integers
    and uses multithreading to print the square and cube of each integer concurrently.
    """
    user_numbers: list[int] = [int(i) for i in input(f"1.\tEnter a list of non-negative integers,\n"
                                                     f"\tseparated by commas: ").split(",")]

    # Create threads for square and cube calculations
    thread_square = threading.Thread(target=calculate_square,
                                     args=(user_numbers,))
    thread_cube = threading.Thread(target=calculate_cube,
                                   args=(user_numbers,))

    # Start the threads
    thread_square.start()
    thread_cube.start()

    # Wait for both threads to complete
    thread_square.join()
    thread_cube.join()


if __name__ == "__main__":
    print(__doc__)
    main()
