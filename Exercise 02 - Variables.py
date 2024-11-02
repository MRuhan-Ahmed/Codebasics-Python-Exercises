"""
Exercise 2 - Variables
https://github.com/codebasics/py/tree/master/Basics/Exercise
"""

from datetime import datetime

# 1. Create a variable called break and assign it a value 5.
# See what happens and find out the reason behind the behavior that you see.s


def question1() -> None:
    """Explains why using 'break' as a variable name causes an error."""
    print("1.\tI get 'SyntaxError: invalid syntax' because break is used in python.")


# 2. Create two variables. One to store your birth year and another one to store
# current year. Now calculate your age using these two variables


def question2() -> None:
    """Calculates and prints the age using birth year and current year."""
    birth_year: int = 2001
    current_year: int = datetime.now().year
    print(f"2.\tMy current age is {(current_year - birth_year)}.")


# 3. Store your first, middle and last name in three different variables
# and then print your full name using these variables


def question3() -> None:
    """Prints the full name by combining first and last name variables."""
    first_name: str = "R"
    last_name: str = "ahmed"
    print(f"3.\tMy name is {first_name}{last_name}.")


# 4. Answer which of these are invalid variable names:
# _nation 1record record1 record_one record-one record^one continue

def question4() -> None:
    """Prints valid variable names."""
    _nation = "1"
    # 1record = "2"     # Invalid
    record1 = "3"
    record_one = "4"
    # record-one= "5"   # Invalid
    # record^one = "6"  # Invalid
    # continue          # Invalid

    print(f"4.\tThe valid variable names are _nation: '{_nation}', "
          f"record1: '{record1}' and record_one: '{record_one}'.")


def main() -> None:
    """Executes all question functions sequentially."""
    question1()
    question2()
    question3()
    question4()


if __name__ == "__main__":
    print(__doc__)
    main()
