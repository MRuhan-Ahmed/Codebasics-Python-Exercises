"""
Exercise 28 - Sharing Data between Processes using Arrays & Values
https://www.youtube.com/watch?v=uWbSc84he2Q
"""

import multiprocessing


def calculate_square(numbers: list[int],
                     square_result: multiprocessing.Array,
                     given_value: multiprocessing.Value) -> None:
    """
    Calculates the square of each number in the provided list and stores
    the results in a shared array. Also updates a shared value.

    :param numbers: A list of integers whose squares are to be calculated.
    :param square_result: A multiprocessing Array where the squares will be stored.
    :param given_value: A multiprocessing Value to be updated within the process.
    """
    given_value.value = 5.67  # Example of updating the shared value
    for index, number in enumerate(numbers):
        print(f"\t{number}² = {number ** 2}")
        square_result[index] = number ** 2  # Store the square in the shared array


def main() -> None:
    """
    Prompts the user to enter a list of integers and calculates their squares
    using multiprocessing. Results are stored in shared memory.
    """
    user_numbers = [int(i) for i in input(f"\tEnter a list of integers,\n"
                                          f"\tseparated by commas: ").split(",")]

    # Create shared memory for results and a shared value
    square_numbers = multiprocessing.Array("i", len(user_numbers))  # Array of integers
    value = multiprocessing.Value("d", 0.0)  # Value of type double

    # Create and start the process to calculate squares
    process1 = multiprocessing.Process(target=calculate_square,
                                       args=(user_numbers, square_numbers, value))
    process1.start()
    process1.join()  # Wait for the process to finish

    # Display results from the shared memory
    print(f"\tOutside the process: {square_numbers[:]}")  # Show calculated squares
    print(f"\tNew value: {value.value}")  # Show updated value


if __name__ == "__main__":
    print(__doc__)
    main()
