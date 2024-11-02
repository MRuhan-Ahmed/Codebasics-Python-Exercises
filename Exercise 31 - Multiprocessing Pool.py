"""
Exercise 31 - Multiprocessing Pool
https://www.youtube.com/watch?v=_1ZwkCY9wxk
"""

from multiprocessing import Pool
import time


def square(number: int) -> int:
    """
    Returns the square of a given integer.

    :param number: The given integer to square
    :return: The square of a given integer
    """
    return number ** 2


def sum_powers(n: int) -> int:
    """
    Returns the sum of squares from 0 to n.

    :param n: The upper bound of the range of integers
    :return: The sum of squares from 0 to n
    """
    return sum(x ** 2 for x in range(n))


def main() -> None:
    """Main function to execute the multiprocessing tasks."""

    # User input for numbers to square
    user_numbers = list(map(int, input("\tEnter a list of integers,\n"
                                       "\tseparated by commas: ").split(",")))

    # Using a Pool to square the numbers
    with Pool(processes=3) as pool:
        results = pool.map(square, user_numbers)
        print(f"\tSquared results: {results}")

    # Measuring time for sum of squares using Pool
    start_time: float = time.time()
    with Pool() as pool:
        pool.map(sum_powers, range(1200))  # Note: Result is not stored as it's not used.
    print(f"\tPool took: {time.time() - start_time:.4f} seconds.")

    # Measuring time for serial processing
    start_time: float = time.time()
    _: list[int] = [sum_powers(x) for x in range(100)]  # Use underscore to indicate unused result.
    print(f"\tSerial processing took: {time.time() - start_time:.4f} seconds.")


if __name__ == "__main__":
    print(__doc__)
    main()
