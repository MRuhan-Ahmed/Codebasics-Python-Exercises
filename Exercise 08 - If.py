"""
Exercise 8 - If
https://github.com/codebasics/py/tree/master/Basics/Exercise
"""


# 1. Using following list of cities per country,
#   india = ["mumbai", "banglore", "chennai", "delhi"]
#   pakistan = ["lahore","karachi","islamabad"]
#   bangladesh = ["dhaka", "khulna", "rangpur"]
# Write a program that asks user to enter a city name.
# It should tell which country the city belongs to
# Write a program that asks user to enter two cities.
# It tells you if they both are in same country or not.
# For example, if I enter mumbai and chennai, it will print "Both cities are in India"
# but if I enter mumbai and dhaka it should print "They don't belong to same country"


def question1() -> None:
    """
    Determines the country of a given city and checks if two cities are in the same country.
    """
    india: list[str] = ["mumbai", "banglore", "chennai", "delhi"]
    pakistan: list[str] = ["lahore", "karachi", "islamabad"]
    bangladesh: list[str] = ["dhaka", "khulna", "rangpur", "sylhet"]

    # Mapping countries to their respective city lists
    countries: dict[str, list[str]] = {
        "India": india,
        "Pakistan": pakistan,
        "Bangladesh": bangladesh
    }

    # Part i: Identify country by city
    user_city: str = input("1.\ti) Enter your city name: ").lower()
    for country, cities in countries.items():
        if user_city in cities:
            print(f"You are from {country}.")
            break
    else:
        print("Country not found.")

    # Part ii: Check if two cities are in the same country
    city_query1: str = input("\n1.\tii) Enter a city name: ").lower()
    city_query2: str = input("Enter another city name: ").lower()

    # Find the country for each city
    country1: str | None = next((country for country, cities in countries.items() if city_query1 in cities), None)
    country2: str | None = next((country for country, cities in countries.items() if city_query2 in cities), None)

    # Check if they are in the same country
    if country1 and country1 == country2:
        print(f"Both cities are in {country1}.")
    else:
        print("They don't belong to the same country.")


# 2. Write a python program that can tell you if your sugar is normal or not.
# Normal fasting level sugar range is 80 to 100.
# i) Ask the user to enter his fasting sugar level
# ii) If it is below 80 to 100 range then print that sugar is low
# iii) If it is above 100 then print that it is high otherwise print that it is normal


def question2() -> None:
    """
    Checks if a user's fasting sugar level is within, below, or above the normal range.
    Normal fasting sugar level range: 80 - 100.
    """
    normal_min: float = 80
    normal_max: float = 100

    user_sugar_level = float(input("\n2. What is your fasting sugar level? "))

    if user_sugar_level < normal_min:
        print("Sugar level is low.")
    elif user_sugar_level > normal_max:
        print("Sugar level is high.")
    else:
        print("Sugar level is normal.")


def main() -> None:
    """Executes all question functions sequentially."""
    question1()
    question2()


if __name__ == "__main__":
    print(__doc__)
    main()
