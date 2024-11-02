"""
Exercise 13 - Reading & Writing Files
https://github.com/codebasics/py/tree/master/Basics/Exercise
"""


# 1. poem.txt contains "Road not taken" by Robert Frost.
# You have to read this file in your python program
# and find out which words have maximum occurrence.


def count_word_occurrences(file_path: str) -> tuple[int, dict[str, int]]:
    """
    Reads a text file and counts occurrences of each word.

    :param file_path: Path to the text file.
    :return: A tuple containing the maximum word count and a dictionary with word counts.
    """
    word_count: dict[str, int] = {}

    with open(file_path, "r") as file:
        for line in file:
            words = line.split()
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1

    maximum_wordcount: int = max(word_count.values(), default=0)
    return maximum_wordcount, word_count


def display_max_occurrences(max_count: int,
                            word_count: dict[str, int]) -> None:
    """
    Prints words that have the maximum occurrence in a file.

    :param max_count: Maximum count of a single word.
    :param word_count: Dictionary of words with their occurrences.
    """
    print(f"1.\tThe maximum occurrence of a given word is: {max_count}")
    print("\tWords with maximum occurrence are: ")
    for word, count in word_count.items():
        if count == max_count:
            print(f"\t{word}")


def question1() -> None:
    max_count, word_count = count_word_occurrences("poem.txt")
    display_max_occurrences(max_count, word_count)


# 2. stocks.csv contains stock price, earnings per share and book value.
# You are writing a stock market application that will process this file
# and create a new file with financial metrics
# such as per ratio and price to book ratio.
# These are calculated as,
# per ratio = price / earnings per-share
# price to book ratio = price / book value
# Your input format (stocks.csv) is,
#
# Company Name  | Price | Earnings Per Share    | Book Value
# Reliance	    | 1467  | 66	                | 653
# Tata Steel	| 391	| 89	                | 572
#
# Output.csv should look like this,
#
# Company Name	| PE Ratio	| PB Ratio
# Reliance	    | 22.23	    | 2.25
# Tata Steel    | 4.39	    | 0.68


def process_stock_data(input_file: str,
                       output_file: str) -> None:
    """
    Processes stock data to calculate financial metrics (PE Ratio and PB Ratio)
    and writes them to an output file.

    :param input_file: Path to the input CSV file with stock data.
    :param output_file: Path to the output CSV file for calculated metrics.
    """
    with open(input_file, "r") as stocks_file, open(output_file, "w") as stock_file_output:
        stock_file_output.write("Company Name, PE Ratio, PB Ratio\n")
        next(stocks_file)  # Skip header
        for line in stocks_file:
            data = line.strip().split(",")
            stock: str = data[0]
            price = float(data[1])
            earnings_per_share = float(data[2])
            book_value = float(data[3])

            price_earnings_ratio: float = round(price / earnings_per_share, 2)
            price_book_ratio: float = round(price / book_value, 2)

            stock_file_output.write(f"{stock}, {price_earnings_ratio}, {price_book_ratio}\n")


def display_file_contents(file_path: str) -> None:
    """
    Reads and prints each line in a file.

    :param file_path: Path to the file to read and display.
    """
    with open(file_path, "r") as file:
        for line in file:
            print(f"2.\t{line.strip()}")


def question2() -> None:
    process_stock_data("stocks.csv", "output.csv")
    display_file_contents("output.csv")


def main() -> None:
    """Executes all question functions sequentially."""
    question1()
    question2()


if __name__ == "__main__":
    print(__doc__)
    main()
