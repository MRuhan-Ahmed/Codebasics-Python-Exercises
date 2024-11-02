"""
Exercise 20 - Iterators
https://github.com/codebasics/py/tree/master/Basics/Exercise
"""

from typing import Iterator


# 1. Create an iterator for fibonacci series in such a way
# that each next returns the next element from fibonacci series.
# 2. The iterator should stop when it reaches a limit defined in the constructor.


class Fibonacci:
    """An iterator for generating the Fibonacci series up to a specified number of terms."""

    def __init__(self, number_of_terms: int) -> None:
        """
        Initializes the Fibonacci iterator.

        :param number_of_terms: The number of terms to generate in the Fibonacci sequence.
        """
        self.number_of_terms: int = number_of_terms
        self.current, self.next = 1, 1
        self.count = 0

    def __iter__(self) -> Iterator[int]:
        """
        Returns an iterator for the Fibonacci series.

        :return: An iterator for the Fibonacci series.
        """
        return self

    def __next__(self) -> int:
        """
        Returns the next number in the Fibonacci series until the number of terms is reached.

        :raises StopIteration: When the end of the specified term limit is reached.
        :return: The next number in the Fibonacci series.
        """
        if self.count >= self.number_of_terms:
            raise StopIteration
        current_result = self.current
        self.current, self.next = self.next, self.current + self.next
        self.count += 1
        return current_result


def main() -> None:
    """
    Accepts user input for the number of Fibonacci terms, creates an iterator, and prints each term.

    :return: None
    """
    print(f"\tThe Fibonacci sequence is defined as:\n\tFₙ = Fₙ₋₁ + Fₙ₋₂, for n > 1")

    try:
        user_input = int(input("\tEnter the number of terms to iterate: "))
        if user_input <= 0:
            raise ValueError("The number of terms must be a positive integer.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    print(f"\tFibonacci sequence up to {user_input} terms:")
    for index, term in enumerate(Fibonacci(user_input), start=1):
        print(f"\tn = {index}\t result: {term}")


# A simpler way to make fibonacci sequence:
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


for f in fib():
    if f > 100:
        break
    print(f)

if __name__ == "__main__":
    print(__doc__)
    main()
