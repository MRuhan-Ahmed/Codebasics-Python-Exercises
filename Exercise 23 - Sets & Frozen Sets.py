"""
Exercise 23 - Sets & Frozen Sets
https://github.com/codebasics/py/tree/master/Basics/Exercise
"""

# 1. create any set and try to use frozenset(set name)


def question1() -> None:
    """Converts a given set of integers to a frozenset and prints it."""
    print(f"1.\tFrozen set: {frozenset({1, 2, 3, 4, 5})}")


# 2. Find the elements in a given set that are not in another set
#
#     set1 = {1,2,3,4,5}
#     set2 = {4,5,6,7,8}
#
#     difference between set1 and set2 is {1,2,3}


def question2() -> None:
    """Calculates and prints elements in a given set, that are not in another set."""
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    print(f"2.\tThe elements in set1 that aren't in set2 are: {(set1 - set2)}")


def main() -> None:
    """Executes all question functions sequentially."""
    question1()
    question2()


if __name__ == "__main__":
    print(__doc__)
    main()
