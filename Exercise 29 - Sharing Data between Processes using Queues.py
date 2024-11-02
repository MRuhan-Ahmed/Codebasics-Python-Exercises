"""
Exercise 29 - Sharing Data between Processes using Queues
https://www.youtube.com/watch?v=sp7EhjLkFY4
"""

import multiprocessing


def calculate_square(numbers: list[int],
                     number_queue: multiprocessing.Queue) -> None:
    """
    Calculates the square of each number in the provided list and puts
    the results into a queue.

    :param numbers: A list of integers whose squares are to be calculated.
    :param number_queue: A multiprocessing Queue where the squared numbers will be stored.
    """
    for number in numbers:
        number_queue.put(number ** 2)


def main() -> None:
    """
    Asks the user to enter a list of integers, calculates their squares
    using multiprocessing, and shares the results through a queue.
    """
    user_numbers = [int(i) for i in input(f"\tEnter a list of integers,\n"
                                          f"\tseparated by commas: ").split(",")]

    # Create a multiprocessing Queue for sharing squared numbers
    queue = multiprocessing.Queue()

    # Create and start the process to calculate squares
    process1 = multiprocessing.Process(target=calculate_square,
                                       args=(user_numbers, queue))
    process1.start()
    process1.join()  # Wait for the process to finish

    # Retrieve and print the squared numbers from the queue
    while not queue.empty():
        print(f"\t{queue.get()}")


if __name__ == "__main__":
    print(__doc__)
    main()
