import sys
import string

def count_characters(text):
    """
    Count the number of upper letters, lower letters, punctuation marks, spaces, and digits in a given text.
    """
    return {
        'upper': sum(1 for c in text if c.isupper()),
        'lower': sum(1 for c in text if c.islower()),
        'punctuation': sum(1 for c in text if c in string.punctuation),
        'spaces': sum(1 for c in text if c.isspace()),
        'digits': sum(1 for c in text if c.isdigit())
    }

def display_counts(text, counts):
    """
    Display the character counts in a formatted manner.
    """
    total_chars = len(text)
    output = f"The text contains {total_chars} characters:\n"
    output += f"{counts['upper']} upper letters\n"
    output += f"{counts['lower']} lower letters\n"
    output += f"{counts['punctuation']} punctuation marks\n"
    output += f"{counts['spaces']} spaces\n"
    output += f"{counts['digits']} digits"
    return output

def process_input(text):
    """
    Process the input text by counting its characters and displaying the results.
    """
    counts = count_characters(text)
    return display_counts(text, counts)

def main():
    """
    Main function to handle input and process it.
    """
    if len(sys.argv) > 2:
        print("AssertionError: too many arguments")
        return
    
    if len(sys.argv) == 2:
        text = sys.argv[1].replace('\n', ' ').replace('-\n', '-')
    else:
        text = input("What is the text to count?\n")
        text += '\n'  # Add newline for input case
    
    result = process_input(text)
    print(result)

if __name__ == "__main__":
    main()
