import sys
from ft_filter import ft_filter


def main():
    """
    Accepts only 2 arguments:
    1. string
    2. integer

    Returns a list of words that are longer than the integer.
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        text = sys.argv[1]
        n = sys.argv[2]

        if not isinstance(text, str):
            raise AssertionError("the argument are bad")

        if not n.isdigit():
            raise AssertionError("the argument are bad")

        n = int(n)

        filt_words = list(ft_filter(lambda word: len(word) > n, text.split()))
        print(filt_words)

    except AssertionError as error:
        print(type(error).__name__ + ":", error)


if __name__ == "__main__":
    main()
