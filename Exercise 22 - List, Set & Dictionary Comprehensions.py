"""
Exercise 22 - List, Set & Dictionary Comprehensions
https://github.com/codebasics/py/tree/master/Basics/Exercise
"""


# 1. Create a Dictionary which contains the Binary values mapping
# with numbers found in the below integer and binary and save it in binary_dict.
# Example :
#
#     integer = [0, 1, 2, 3, 4]
#     binary = ["0", "1", "10", "11", "100"]
#     binary_dict = {0:"0", 1:"1", 2:"10", 3: "11", 4:"100"}

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(even_numbers := [i for i in numbers if i % 2 == 0])
# print(square_numbers := [i ** 2 for i in numbers])

def integer_binary_map(max_range: int) -> dict[int, str]:
    """
    Generates a dictionary mapping integers from 0 to max_range to their binary equivalents.

    :param max_range: The upper limit of integers to include in the dictionary.
    :return: A dictionary where keys are integers and values are their binary string equivalents.
    """
    return {i: bin(i) for i in range(max_range + 1)}


def question1() -> None:
    """
    Asks the user to enter a maximum range of integers,
    then displays a dictionary that maps each integer within [0, range] to its binary representation.
    """
    max_range = int(input("1.\tEnter a maximum range to map integers to their binary equivalence: "))
    print(f"\t{integer_binary_map(max_range)}\n")


# 2. Create a List which contains additive inverse of a given integer list.
# An additive inverse a for an integer i is a number such that:
# a + i = 0
# Example:
#
# integer = [1, -1, 2, 3, 5, 0, -7]
# additive_inverse = [-1, 1, -2, -3, -5, 0, 7]

def additive_inverse(integers: list[int]) -> list[int]:
    """
    Returns the additive inverse for each integer in a given list.

    :param integers: List of integers.
    :return: A list of additive inverses.
    """
    return [-num for num in integers]


def question2() -> None:
    """
    Asks the user to enter a list of integers,
    then displays both the original list and a list containing the additive inverse of each integer.
    """
    numbers = [int(i) for i in input("2.\tEnter a list of integers, separated by commas: ").split(",")]
    print(f"\tOriginal list: {numbers}\n"
          f"\tAdditive inverses: {additive_inverse(numbers)}\n")


# 3. Create a set which only contains unique squares from a given integer list.
# integer = [1, -1, 2, -2, 3, -3]
# sq_set = {1, 4, 9}

def unique_squares(integers: list[int]) -> set[int]:
    """
    Generates a set containing the unique squares of integers in a given list.

    :param integers: List of integers.
    :return: A set containing unique squares of the integers.
    """
    return {num ** 2 for num in integers}


def question3() -> None:
    """
    Asks the user to enter a list of integers,
    then displays both the original list and a set containing the unique squares of each integer.
    """
    list_of_numbers = [int(j) for j in input("3.\tEnter a list of integers, separated by commas: ").split(",")]
    print(f"\tOriginal list: {list_of_numbers}\n"
          f"\tUnique squares: {unique_squares(list_of_numbers)}")


def main() -> None:
    """Executes all question functions sequentially."""
    question1()
    question2()
    question3()


if __name__ == "__main__":
    print(__doc__)
    main()
