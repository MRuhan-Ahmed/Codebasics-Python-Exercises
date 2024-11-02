"""
Exercise 12 - Walrus Operator
FAKE EXERCISE - made using ChatGPT
"""


def example1() -> None:
    """
    Example 1: Demonstrates basic usage of the walrus operator to
    assign a value and print it in a single step.
    """
    print(example1.__doc__)
    value = 10
    print(f"Without walrus operator: {value}")

    # Using the walrus operator to do both at once
    print(f"With walrus operator: {(value := 20)}")  # Changes value to 20 and prints it


def example2() -> None:
    """
    Example 2: Uses the walrus operator in a `while` loop to
    accept user input until the user enters 'exit'.
    """
    print(example2.__doc__)

    while (user_input := input("Enter something (or 'exit' to quit): ")) != 'exit':
        print(f"You entered: {user_input}")


def example3() -> None:
    """
    Example 3: Uses the walrus operator in a list comprehension to
    filter a list of numbers, keeping only even numbers.
    """
    print(example3.__doc__)

    numbers: list[int] = [1, 2, 3, 4, 5, 6]
    evens: list[int] = [num for num in numbers if (is_even := num % 2 == 0)]
    print(f"Even numbers: {evens}")


def example4() -> None:
    """
    Example 4: Uses the walrus operator within a conditional expression
    to find and print the first word in a list that has more than 5 letters.
    """
    print(example4.__doc__)

    words: list[str] = ["apple", "banana", "kiwi", "strawberry"]
    first_long_word: str = next((word for word in words if (length := len(word)) > 5), None)
    print(f"The first word with more than 5 letters is: {first_long_word}")


def example5() -> None:
    """
    Example 5: Demonstrates using the walrus operator as part of a function argument,
    which takes user input, assigns it, and passes it to a function in one line.
    """
    print(example5.__doc__)

    def square(x: int) -> int:
        """Returns the square of a given integer x."""
        return x ** 2

    # Without walrus operator
    value = int(input("Enter a number to square: "))
    print(f"Square without walrus operator: {square(value)}")

    # With walrus operator
    print(f"Square with walrus operator: {square(value := int(input('Enter a number to square: ')))}")


def example6() -> None:
    """
    Example 6: Demonstrates using the walrus operator in a Fibonacci sequence generator,
    where the next Fibonacci number is calculated and printed until it exceeds 100.
    """
    print(example6.__doc__)
    a, b = 0, 1
    while (next_value := a + b) <= 100:
        print(next_value, end=" ")
        a, b = b, next_value


def main() -> None:
    """Executes each example sequentially
    to demonstrate the walrus operator in different use cases."""
    example1()
    example2()
    example3()
    example4()
    example5()
    example6()


if __name__ == "__main__":
    print(__doc__)
    main()
