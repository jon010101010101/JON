
import sys


def analyze_string(text):
    """
    text (input string): The text to analyze

    Prints the following information:
    1. The number of characters in the text
    2. The number of upper case letters
    3. The number of lower case letters
    4. The number of punctuation marks
    5. The number of spaces
    6. The number of digits
    """
    char_count = len(text)
    upper_count = sum(c.isupper() for c in text)
    lower_count = sum(c.islower() for c in text)
    punctuation_marks = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    punctuation_cnt = sum(1 for char in text if char in punctuation_marks)
    space_count = sum(c.isspace() for c in text)
    digit_count = sum(c.isdigit() for c in text)

    print(f"The text contains {char_count} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_cnt} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


def main():
    """
    Analyzes the given text and prints information about its char composition.

    Asks for input if no argument is given:

    raises AssertionError: Too many arguments provided
    """
    try:
        if len(sys.argv) < 2:
            try:
                s = input("What is the text to count?\n")
                s += "\n"
            except EOFError:
                pass
        elif len(sys.argv) == 2:
            s = sys.argv[1]
        elif len(sys.argv) > 2:
            raise AssertionError("Too many arguments provided")
        analyze_string(s)
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()
