"""
Exercise 9 - For
https://github.com/codebasics/py/tree/master/Basics/Exercise
"""


# 1. After flipping a coin 10 times you get the following results:
# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# Use a for loop to figure out how many times you get heads


def question1() -> None:
    """Counts the number of "heads" in a given list of coin flip results."""
    result: list[str] = ["heads", "tails", "tails", "heads", "tails",
                         "heads", "heads", "tails", "tails", "tails"]
    number_of_heads: int = sum(1 for flip in result if flip == "heads")
    print(f"1.\tThere are {number_of_heads} heads flipped out of 10 times.")


# 2. Print all square numbers between 1 and 100, except even_numbers numbers


def question2() -> None:
    """Prints all square numbers between 1 and 100 for odd numbers only."""
    print("2.\tOdd square numbers between 1 and 100:")
    for number in range(1, 11):
        if number % 2 != 0:
            print(f"\t{number ** 2}")


# 3. Your monthly expense list (from Jan to May) looks like this,
# expense_list = [2340, 2500, 2100, 3100, 2980]
# Write a program that asks you to enter an expense amount and
# the program should tell you in which month that expense occurred.
# If the expense is not found then it should print that as well.


def question3() -> None:
    """
    Finds the month corresponding to a given expense amount from a list of monthly expenses.
    """
    expense_list: list[int] = [2340, 2500, 2100, 3100, 2980]
    months_list: list[str] = ["January", "February", "March", "April", "May"]
    expense_amount = int(input("3.\tEnter your expense amount: "))

    if expense_amount in expense_list:
        month_index: int = expense_list.index(expense_amount)
        print(f"\tYou spent ${expense_amount} in {months_list[month_index]}.")
    else:
        print("\tMonth of expense not found.")


# 4. Let's say you are running a 5 km race. Write a program that,
# Upon completing each 1 km asks you "are you tired?"
# If you reply "yes"
#   then it should break and print "you didn't finish the race"
# If you reply "no"
#   then it should continue and ask "are you tired" on every km
# If you finish all 5 km
#   then it should print a congratulations message


def question4() -> None:
    """
    Simulates a 5 km race, asking the user at each km if they are tired.
    If they answer "yes", the race stops. If they complete the race, congratulates them.
    """
    race_length: int = 5
    distance_travelled: int = 0

    for kilometer in range(race_length):
        response: str = input(f"4.\tYou've completed {kilometer} km. Are you tired? ").lower()
        if response == "yes":
            print("\tYou didn't finish the race.")
            break
        elif response == "no":
            distance_travelled += 1

    if distance_travelled == race_length:
        print("\tCongratulations on completing the race!")


# 5. Write a program that prints following shape
# *
# **
# ***
# ****
# *****


def question5() -> None:
    """
    Prints a triangle pattern with increasing number of asterisks for 5 lines.
    """
    print("5.\tTriangle Pattern:")
    for i in range(1, 6):
        print(f"\t{'*' * i}")


def main() -> None:
    """Executes all question functions sequentially."""
    question1()
    question2()
    question3()
    question4()
    question5()


if __name__ == "__main__":
    print(__doc__)
    main()
