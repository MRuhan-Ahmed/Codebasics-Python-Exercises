"""
Exercise 4 - Strings
https://github.com/codebasics/py/tree/master/Basics/Exercise
"""


# 1. Create 3 variables to store street, city and country,
# now create an address variable to store entire address.
# Use two methods to create this variable,
# one using the + operator and the other using f-string.
# Now Print the address in such a way that the
# street, city and country prints in a separate line


def question1() -> None:
    """
    Creates and prints an address by combining street, city, and country variables.
    Uses both concatenation and f-string methods.
    """
    street: str = "Oxford street"
    city: str = "London"
    country: str = "Spain"
    # address_method1: str = street + ", " + city + ", " + country
    # address_method2: str = f"{street}, {city}, {country}"

    print(f"1.\t{street},\n\t{city},\n\t{country}")


# 2. Create a variable to store the string "Earth revolves around the sun"
# i) Print "revolves" using slice operator
# ii) Print "sun" using negative index


def question2() -> None:
    """Slices and prints parts of a string to display specific words."""
    earth_fact = "Earth revolves around the sun"

    print(f"2.\ti) {earth_fact[6:15]}\n\tii) {earth_fact[-3:]}")


# 3. Create two variables to store how many fruits and vegetables you eat in a day.
# Now Print "I eat x veggies and y fruits daily"
# where x and y presents vegetables and fruits that you eat every day.
# Use python f string for this.


def question3() -> None:
    """Prints a statement about daily consumption of fruits and vegetables."""
    fruits_per_day: int = 2
    vegetables_per_day: int = 4
    print(f"3.\tI eat {vegetables_per_day} veggies and {fruits_per_day} fruits daily.")


# 4. I have a string variable called s='maine 200 banana khaye'.
# This of course is a wrong statement; the correct statement is 'maine 10 samosa khaye'.
# Replace incorrect words in the original string with new ones and print the new string.
# Also try to do this in one line.


def question4() -> None:
    """Replaces incorrect words in a string to form a new, corrected statement."""
    s = "maine 200 banana khaye"
    print(f"4.\t{s.replace("banana", "samosa").replace("200", "10")}.")


def main() -> None:
    """Executes all question functions sequentially."""
    question1()
    question2()
    question3()
    question4()


if __name__ == "__main__":
    print(__doc__)
    main()
