"""
Exercise 5 - Lists
https://github.com/codebasics/py/tree/master/Basics/Exercise
"""


# 1. Let us say your expense for every month are listed below,
#   January - 2200
#   February - 2350
#   March - 2600
#   April - 2130
#   May - 2190
# Create a list to store these monthly expenses and using that find out:
#   1. In Feb, how many dollars you spent extra compare to January?
#   2. Find out your total expense in first quarter (first three months) of the year.
#   3. Find out if you spent exactly 2000 dollars in any month
#   4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
#   5. You returned an item that you bought in a month of April and
#   got a refund of 200$. Make a correction to your monthly expense list
#   based on this


def question1() -> None:
    """
    Analyzes monthly expenses to:
    1) Calculate extra dollars spent in February compared to January.
    2) Compute total expenses for the first quarter.
    3) Check if exactly $2000 was spent in any month.
    4) Add June expenses to the list.
    5) Adjust April expenses due to a refund.
    """

    expenses = [
        2200,   # January
        2350,   # February
        2600,   # March
        2130,   # April
        2190    # May
        ]

    # 1. Extra dollars spent in February compared to January
    print(f"1.\ti)\t I spent ${(expenses[1] - expenses[0])} extra in February compared to January.")

    # 2. Total expenses in the first quarter
    print(f"\tii)\t My total expense in the first quarter is ${sum(expenses[:3])}.")

    # 3. Check if exactly $2000 was spent in any month
    print(f"\tiii) {'I have' if 2000 in expenses else 'I have not'} spent exactly $2000 in any month.")

    # 4. Add June expense
    expenses.append(1980)
    print(f"\tiv)\t I spent ${expenses[-1]} in June.")

    # 5. Adjust April expense due to a $200 refund
    expenses[3] -= 200
    print(f"\tv)\t I spent ${expenses[3]} in April (after refund adjustment).\n")

# 2. You have a list of your favourite marvel super heroes.
#   heroes=['Spider-Man','thor','hulk','iron man','captain america']
# Using this find out,
#   1. Length of the list
#   2. Add 'black panther' at the end of this list
#   3. You realize that you need to add 'black panther' after 'hulk',
#   so remove it from the list first and then add it after 'hulk'
#   4. Now you don't like thor and hulk because they get angry easily :)
#   So you want to remove thor and hulk from list and replace them with doctor strange.
#   Do that with one line of code.
#   5. Sort the heroes list in alphabetical order
#   (Hint. Use dir() functions to list down all functions available in list)


def question2() -> None:
    """
    Performs operations on a list of favorite heroes:
    1) Finds list length.
    2) Adds 'black panther' to the end of the list.
    3) Moves 'black panther' to be placed after 'hulk'.
    4) Replaces 'thor' and 'hulk' with 'doctor strange'.
    5) Sorts the list alphabetically.
    """
    heroes = ["spider man", "thor", "hulk", "iron man", "captain america"]

    # 1. Length of the list
    print(f"2.\ti)\t The length of the list is {len(heroes)}.")

    # 2. Add 'black panther' at the end
    heroes.append("black panther")
    print(f"\tii)\t {heroes}")

    # 3. Move 'black panther' to be after 'hulk'
    heroes.remove("black panther")
    heroes.insert(3, "black panther")
    print(f"\tiii) {heroes}")

    # 4. Replace 'thor' and 'hulk' with 'doctor strange'
    heroes[1:3] = ["doctor strange"]
    print(f"\tiv)\t {heroes}")

    # 5. Sort heroes alphabetically
    heroes.sort()
    print(f"\tv)\t {heroes}")


def main() -> None:
    """Executes all question functions sequentially."""
    question1()
    question2()


if __name__ == "__main__":
    print(__doc__)
    main()
