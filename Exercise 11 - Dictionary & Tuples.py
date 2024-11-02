"""
Exercise 11 - Dictionary & Tuples
https://github.com/codebasics/py/tree/master/Basics/Exercise
"""
import math

# 1. We have the following information on countries
# and their population (population is in 10 million),
#
# Country   | Population
# China     | 143
# India     | 136
# USA       | 32
# Pakistan  | 21
# Using above create a dictionary of countries and its population
# Write a program that asks user for three type of inputs:
# A. print: if user enter print
#       then it should print all countries with their population in this format,
#           china==>143
#           india==>36
#           usa==>32
#           pakistan==>21
# B. add: if user input add
#       then it should further ask for a country name to add.
#   If country already exist in our dataset
#       then it should print that it exist and do nothing.
#   If it doesn't then it asks for population
#       and add that new country/population in our dictionary and print it
# C. remove: when user inputs
#       remove it should ask for a country to remove.
#   If country exist in our dictionary
#       then remove it and print new dictionary using format shown above in (a). Else print that country doesn't exist!
# D. query: on this again ask user
#   for which country he or she wants to query.
#   When user inputs that country it will print population of that country.


def print_population(population_dict: dict[str, int]) -> None:
    """
    Prints each country and its population in a formatted list.

    :param population_dict: Dictionary of countries and their populations
    """
    for country, population in population_dict.items():
        print(f"\t{country.lower()}==>{population}")


def add_country(country_dict: dict[str, int]) -> None:
    """
    Adds a country and its population to the dictionary if it does not already exist.

    :param country_dict: Dictionary of countries and their populations
    """
    country: str = input("\tWhat country do you want to add? ").capitalize()
    if country in country_dict:
        print(f"\t{country} already exists in the dictionary.")
    else:
        population = int(input(f"\tEnter the population of {country}: "))
        country_dict[country] = population
        print_population(country_dict)


def remove_country(country_dict: dict[str, int]) -> None:
    """
    Removes a specified country from the dictionary if it exists.

    :param country_dict: Dictionary of countries and their populations
    """
    country: str = input("\tWhat country do you want to remove? ").capitalize()
    if country not in country_dict:
        print(f"\t{country} doesn't exist in the dictionary.")

    del country_dict[country]
    print_population(country_dict)


def query_country(country_dict: dict[str, int]) -> None:
    """
    Queries and prints the population of a specified country if it exists.

    :param country_dict: Dictionary of countries and their populations
    """
    country: str = input("\tWhat country do you want to query? ").capitalize()
    print(f"\t{country.lower()}==>{country_dict.get(country, 'Not found')}")


def question1() -> None:
    """
    Manages a population dictionary, allowing users to print, add, remove, or query countries.
    """
    population_to_country: dict[str, int] = {
        "China": 143,
        "India": 136,
        "Usa": 32,
        "Pakistan": 21
    }

    action: str = input("1.\tType: Print | Add | Remove | Query\n\t").lower()
    if action == "print":
        print_population(population_to_country)
    elif action == "add":
        add_country(population_to_country)
    elif action == "remove":
        remove_country(population_to_country)
    elif action == "query":
        query_country(population_to_country)
    else:
        print("\tInvalid option. Please enter one of: Print, Add, Remove, Query.")


# 2. You are given following list of stocks
# and their prices in last 3 days,
#
# Stock | Prices
# info	| [600,630,620]
# ril	| [1430,1490,1567]
# mtl	| [234,180,160]
# Write a program that asks user for operation.
# Value of operations could be,
# print: When user enters print it should print following,
#   info ==> [600, 630, 620] ==> avg:  616.67
#   ril ==> [1430, 1490, 1567] ==> avg:  1495.67
#   mtl ==> [234, 180, 160] ==> avg:  191.33
# add: When user enters 'add',
#   it asks for stock ticker and price.
#   If stock already exist in your list (like info, ril etc.)
#   then it will append the price to the list.
#   Otherwise, it will create new entry in your dictionary.
#   For example entering 'tata' and 560
#   will add tata ==> [560] to the dictionary of stocks.


def print_prices(prices_dict: dict[str, list[float]]) -> None:
    """
    Prints each stock ticker with its list of prices and average price.

    :param prices_dict: Dictionary of stock tickers and their price lists
    """
    for stock, prices in prices_dict.items():
        average_price: float = round(sum(prices) / len(prices), 2)
        print(f"\t{stock} ==> {prices} ==> avg: {average_price}")


def add_prices(prices_dict: dict[str, list[float]]) -> None:
    """
    Adds a new price to an existing stock or creates a new stock entry.

    :param prices_dict: Dictionary of stock tickers and their price lists
    """
    stock: str = input("Enter the stock ticker: ").lower()
    try:
        price = float(input("Enter price: "))
        prices_dict.setdefault(stock, []).append(price)
        print_prices(prices_dict)
    except ValueError:
        print("\tInvalid price input. Please enter a valid number.")


def question2() -> None:
    """Manages stock prices by allowing user to print or add prices."""
    stock_to_prices: dict[str, list[float]] = {
        "inf": [600, 630, 620],
        "ril": [1430, 1490, 1567],
        "mrl": [234, 180, 160],
    }

    user_input: str = input("2.\tType: Print | Add\n\t").lower()
    if user_input == "print":
        print_prices(stock_to_prices)
    elif user_input == "add":
        add_prices(stock_to_prices)
    else:
        print("\tInvalid option. Please enter 'Print' or 'Add'.")


# 3. Write circle_calc() function that takes radius of a circle
# as an input from user,then calculates and returns the area,
# circumference and diameter.
# You should get these values in your main program
# by calling circle_calc function and then print them


def circle_calc(radius: float) -> tuple[float, float, float]:
    """
    Calculates area, circumference, and diameter of a circle with the given radius.

    :param radius: Radius of the circle
    :return: Tuple containing (area, circumference, diameter)
    """
    area: float = math.pi * (radius ** 2)
    circumference: float = 2 * math.pi * radius
    diameter: float = 2 * radius
    return area, circumference, diameter


def question3() -> None:
    """
    Prompts the user for radius and prints the area, circumference, and diameter of a circle.
    """
    user_radius = float(input(f"3.\tEnter a circle's radius: "))
    
    area, circumference, diameter = circle_calc(user_radius)
    print(f"\tThe area of the circle is: {area}\n"
          f"\tThe circumference of the circle is: {circumference}\n"
          f"\tThe diameter of the circle is {diameter}")


def main() -> None:
    """Executes all question functions sequentially."""
    question1()
    question2()
    question3()


if __name__ == "__main__":
    print(__doc__)
    main()
