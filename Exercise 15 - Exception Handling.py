"""
Exercise 15 - Exception Handling
https://github.com/codebasics/py/tree/master/Basics/Exercise
"""


def main() -> None:
    """
    Main function to execute the division of two user-provided integers.
    Handles exceptions for division and input errors.
    """
    # As of typing, there are no exercises
    # so code is from the YouTube playlist
    # with ChatGPT edits

    z = None  # Initialise z

    try:
        x = float(input("Enter value for x: "))
        y = float(input("Enter value for y: "))

        z = x / y

    except ZeroDivisionError:
        print("You can't divide by zero!")
    except ValueError:
        print("Please enter valid numbers.")
    except Exception as error:
        print(f"Exception occurred: {type(error).__name__}")

    if z is not None:
        print(f"x / y = {z}")


if __name__ == "__main__":
    print(__doc__)
    main()
