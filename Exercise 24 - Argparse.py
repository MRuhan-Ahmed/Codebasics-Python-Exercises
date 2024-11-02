"""
Exercise 24 - Argparse
https://github.com/codebasics/py/tree/master/Basics/Exercise
"""
import argparse

# 1. Take subject marks as command line arguments
# example:
#     python3 cmd.py --physics 60 --chemistry 70 --maths 90


def parse_arguments() -> argparse.Namespace:
    """
    Parses command-line arguments for subject marks.

    :return: An argparse.Namespace object containing parsed arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--physics", help="Physics marks", type=int, required=True)
    parser.add_argument("--chemistry", help="Chemistry marks", type=int, required=True)
    parser.add_argument("--maths", help="Mathematics marks", type=int, required=True)

    return parser.parse_args()


# 2. Find average marks for the three subjects using command line input of marks.

def calculate_average(*marks: int) -> float:
    """
    Calculates the average of the given marks.

    :param marks: The marks of the subjects as integers.
    :return: The average mark as a float.
    """
    return sum(marks) / len(marks)


def main() -> None:
    """Parses arguments from cmd and prints subject marks with their average."""
    args = parse_arguments()

    print(f"1.\tPhysics: {args.physics}\n"
          f"\tChemistry: {args.chemistry}\n"
          f"\tMathematics: {args.maths}")

    average_mark = calculate_average(args.physics, args.chemistry, args.maths)
    print(f"2.\tThe average mark is: {average_mark:.2f}")


if __name__ == "__main__":
    print(__doc__)
    main()
