"""
Exercise 30 - Multiprocessing Lock
https://www.youtube.com/watch?v=POL7n754JTc
"""

import time
import multiprocessing


def update_balance(current_balance: multiprocessing.Value,
                   lock: multiprocessing.Lock,
                   change: int) -> None:
    """
    Updates the current balance by a specified amount while acquiring a lock
    to prevent race conditions.

    :param current_balance: A multiprocessing Value representing the current balance.
    :param lock: A Lock object to ensure that the operation is thread-safe.
    :param change: The amount to change the balance (positive for deposit, negative for withdrawal).
    """
    for _ in range(100):
        time.sleep(0.01)  # Simulate a delay in processing
        with lock:
            current_balance.value += change  # Safely update the balance


def main() -> None:
    """Initialises balance and creates processes for deposit and withdrawal."""
    balance = multiprocessing.Value('i', 200)
    lock = multiprocessing.Lock()

    # Create processes for deposit (increase) and withdrawal (decrease)
    processes: list[multiprocessing] = [
        multiprocessing.Process(target=update_balance,
                                args=(balance, lock, 1)),
        multiprocessing.Process(target=update_balance,
                                args=(balance, lock, -1))
    ]

    # Start and join the processes
    for process in processes:
        process.start()
    for process in processes:
        process.join()

    print(balance.value)


if __name__ == "__main__":
    print(__doc__)
    main()
