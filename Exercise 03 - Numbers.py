"""
Exercise 3 - Numbers
https://github.com/codebasics/py/tree/master/Basics/Exercise
"""

# 1. You have a football field that is 92 meters long and 48.8 meters wide.
# Find out total area using python and print it.


def question1() -> None:
    """Calculate and print the area of a football field that is 92 meters long and 48.8 meters wide."""
    field_length: int = 92
    field_width: float = 48.8
    field_area = round(field_length * field_width, 1)
    print(f"1.\tThe area of the football field is {field_area}m².")


# 2. You bought 9 packets of potato chips from a store.
# Each packet costs 1.49 dollars, and you gave the shopkeeper 20 dollars.
# Find out using python, how many dollars is the shopkeeper going to give you back?


def question2() -> None:
    """Calculate and print the change returned after buying 9 packets of chips at $1.49 each with $20."""
    number_of_packets: int = 9
    packet_cost: float = 1.49
    payment: float = 20.00
    change = round(payment - (number_of_packets * packet_cost), 2)
    print(f"2.\tThe shopkeeper will give back ${change:.2f}.")


# 3. You want to replace tiles in your bathroom which is exactly square
# and 5.5 feet is its length. If tiles cost 500 rs per square feet,
# how much will be the total cost to replace all tiles?
# Calculate and print the cost using python
# (Hint: Use power operator ** to find area of a square)


def question3() -> None:
    """
    Calculate and print the cost to replace tiles in a square bathroom of 5.5 feet length if each tile costs 500 rs.
    """
    tile_length: float = 5.5
    tile_cost_per_square_feet: int = 500
    total_tile_cost = (tile_length ** 2) * tile_cost_per_square_feet
    print(f"3.\tThe total cost to replace all the tiles {total_tile_cost:.2f} rs.")


# 4. Print the binary representation of number 17


def question4() -> None:
    """Print the binary representation of the number 17."""
    print(f"4.\tThe binary representation of 17 is {bin(17)}.")


def main() -> None:
    """Executes all question functions sequentially."""
    question1()
    question2()
    question3()
    question4()


if __name__ == "__main__":
    print(__doc__)
    main()
