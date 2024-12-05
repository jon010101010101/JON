"""Create a script that takes a number as an argument, checks if it is even or odd, and
prints the result.
If more than one argument is provided or if the argument is not an integer, print an AssertionError.
"""
import sys  # Imports the sys module

def main():  # Entry point of the program
    # Checks if exactly one argument is provided
    if len(sys.argv) != 2:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        else:
            print('$')
            return  # Ends the function if no argument is provided

    # Tries to convert the argument to an integer
    try:  # Starts executing code
        number = int(sys.argv[1])  # Tries to convert the first argument to an integer
    except ValueError:
        raise AssertionError("argument is not an integer")

    # Checks if the number is even or odd
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


if __name__ == "__main__":
    main()

