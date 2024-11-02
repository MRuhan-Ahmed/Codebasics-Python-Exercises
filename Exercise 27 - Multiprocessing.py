"""
Exercise 27 - Multiprocessing
https://www.youtube.com/watch?v=Lu5LrKh1Zno
"""

import time
import multiprocessing


def calculate_square(numbers: list[int]) -> None:
    """
    Calculates and prints the square of each number in the provided list
    and stores the results in a global list.

    :param numbers: A list of integers whose squares are to be calculated.
    """
    square_numbers = []
    for number in numbers:
        time.sleep(1)  # Simulate a time-consuming calculation
        print(f"\t{number}² = {number ** 2}")
        square_numbers.append(number ** 2)

    print(f"\tSquare numbers within a process: {square_numbers}")


def calculate_cube(numbers: list[int]) -> None:
    """
    Calculates and prints the cube of each number in the provided list.

    :param numbers: A list of integers whose cubes are to be calculated.
    """
    for number in numbers:
        time.sleep(1)  # Simulate a time-consuming calculation
        print(f"\t{number}³ = {number ** 3}")


def main() -> None:
    """
    Asks the user to enter a list of integers,
    then uses multiprocessing to calculate and print the squares and cubes of each integer concurrently.
    """
    user_numbers = [int(i) for i in input(f"\tEnter a list of integers,"
                                          f"separated by commas: ").split(",")]

    # Create processes for square and cube calculations
    process1 = multiprocessing.Process(target=calculate_square,
                                       args=(user_numbers,))
    process2 = multiprocessing.Process(target=calculate_cube,
                                       args=(user_numbers,))

    # Start the processes
    process1.start()
    process2.start()

    # Wait for both processes to complete
    process1.join()
    process2.join()

    print("\tCompleted!")


if __name__ == "__main__":
    print(__doc__)
    main()
