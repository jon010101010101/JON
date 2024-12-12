from typing import Any, Callable


def square(x: int | float) -> int | float:
    """
    Returns the square of x.

    Args:
        x (int | float): The number to be squared.

    Returns:
        int | float: The square of the input number.
    """
    return x ** 2


def pow(x: int | float) -> int | float:
    """
    Returns x raised to the power of x.

    Args:
        x (int | float): The base and the exponent.

    Returns:
        int | float: The result of raising x to the power of x.
    """
    return x ** x


def outer(
    x: int | float,
    function: Callable[[int | float], Any]
) -> Callable[[], float]:
    """
    Creates a callable that applies a specified function to an initial value
    each time it is called, returning the result of that function.

    Args:
        x (int | float): The initial value to be processed.
        function (Callable[[int | float], Any]): A function that takes a number
                                                 and returns a number.

    Returns:
        Callable[[], float]: A callable object that returns the result of
                             applying the function to the previous result.
    """

    # Initialize the counter and previous result
    count = 0
    previous_result = x

    def inner() -> float:
        """
        Internal function that applies the given function to the previous
         result.

        Returns:
            float: The result of applying the function to the previous result.
            None: If an error occurs during calculation.
        """
        nonlocal count, previous_result
        count += 1  # Increment the counter each time inner is called

        # Error handling to ensure previous_result is numeric
        if not isinstance(previous_result, (int, float)):
            print("ERROR: The previous result is not numeric.")
            return None

        # Calculate the result using the provided function
        result = function(previous_result)

        # Error handling to ensure the result is numeric
        if not isinstance(result, (int, float)):
            print("ERROR: The result of the function is not numeric.")
            return None

        # Update previous_result for the next call
        previous_result = result
        return result

    return inner
