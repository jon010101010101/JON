"""
Filters words from a string based on their length.

Usage: python3 filterstring.py 'string of text' minimum_length

Example: python3 filterstring.py 'Hello the World' 3
"""

import sys


def ft_filter(func, iterable):
    """
    Filters the elements of the iterable according to the provided function.

    Args:
        func: Function that determines if an element should be included.
        iterable: Iterable to filter.

    Returns:
        List of elements that meet the condition.
    """
    return [item for item in iterable if func(item)]


def main():
    """
    Main function that processes command line arguments,
    filters the words, and displays the result.

    Raises:
        AssertionError: If the provided arguments are incorrect.
    """
    try:
        # Check that exactly two arguments are provided
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        # Assign the first argument (the string) to the variable sentence
        sentence = sys.argv[1]

        try:
            # Convert the second argument to an integer and assign it to length
            length = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        # Split the string into words
        words = sentence.split()

        # Filter the words using ft_filter and a lambda expression
        filtered_words = ft_filter(lambda word: len(word) >= length, words)

        # Print the filtered words
        print(filtered_words)

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
