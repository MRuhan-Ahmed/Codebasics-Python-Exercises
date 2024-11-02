"""
Exercise 10 - Functions
https://github.com/codebasics/py/tree/master/Basics/Exercise
"""


# 1. Write a function called calculate_area
# that takes base and height as an input and outputs the area of a triangle.
# Equation of the area of a triangle is,
# area = (1/2)*base*height


def calculate_area(base: float, height: float) -> float:
    """
    Calculates the area of a triangle using the formula (1/2) * base * height.

    :param base: The base of the triangle
    :param height: The height of the triangle
    :return: Area of the triangle
    """
    return 0.5 * base * height


def question1() -> None:
    """
    Asks the user for base and height, calculates, and displays the area of a triangle.
    """
    triangle_base = float(input("1.\tEnter the base of the triangle: "))
    triangle_height = float(input("\tEnter the height of the triangle: "))
    area: float = calculate_area(triangle_base, triangle_height)
    print(f"\tThe area of the triangle is {area} m².")


# 2. Modify the above function to take third parameter shape type.
# It can be either "triangle" or "rectangle".
# Based on shape type it will calculate area.
# Equation of a rectangle's area is, rectangle area=length*width
# If no shape is supplied then it should take triangle as a default shape


def calculate_area2(shape: str, base: float, height: float) -> float:
    """
    Calculates the area based on shape type: 'triangle' or 'rectangle'.
    Defaults to triangle if shape is not specified.

    :param shape: The type of shape ('triangle' or 'rectangle')
    :param base: The base/length of the shape
    :param height: The height/width of the shape
    :return: Area of the specified shape
    """
    if shape == "triangle":
        return 0.5 * base * height
    elif shape == "rectangle":
        return base * height
    else:
        raise ValueError("Invalid shape type. Type 'triangle' or 'rectangle'.")


def question2() -> None:
    """
    Asks the user for shape type, base, and height, then calculates and displays the area.
    """
    user_shape = input("\n2.\tEnter the shape of the area to calculate (triangle/rectangle): ").lower() or "triangle"
    shape_base = float(input(f"\tEnter the base of the {user_shape}: "))
    shape_height = float(input(f"\tEnter the height of the {user_shape}: "))
    area: float = calculate_area2(user_shape, shape_base, shape_height)
    print(f"\tThe area of the {user_shape} is {area} m².")


# 3. Write a function called print_pattern that takes
# integer number as an argument and prints following pattern
# if input number is 3,
#   *
#   **
#   ***
# if input is 4 then it should print
#
#   *
#   **
#   ***
#   ****
# Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)


def print_pattern(lines: int) -> None:
    """
    Prints a pattern of asterisks,
    where the number of lines corresponds to the input number.

    :param lines: The number of lines in the pattern
    """
    for i in range(lines):
        print(f"\t{'*' * i}")


def question3() -> None:
    """
    Asks the user for an integer and prints a triangle pattern of asterisks with that number of lines.
    """
    print_input = int(input("\n3.\tEnter an integer to print the pattern: "))
    print_pattern(print_input)


def main() -> None:
    """Executes all question functions sequentially."""
    question1()
    question2()
    question3()


if __name__ == "__main__":
    print(__doc__)
    main()
