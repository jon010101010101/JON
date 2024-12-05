from typing import Any, Callable

"""
Use of Wrappers:

    The function limit_function acts as a wrapper around the original
    function. It checks the call count, and if the limit has not been
    reached, it executes the original function; otherwise, it prints
    an error message.
    Wrappers are useful for adding functionality (such as counting
    calls) while preserving the original behavior of the function.
"""


def callLimit(limit: int):
    """
    Decorator that limits the number of times a function can be called.

    Args:
        limit (int): The maximum number of times the decorated function
        is allowed to be called.

    Returns:
        Callable: A decorator that applies the limitation to the function.
    """

    count = 0  # Counter to keep track of calls

    def callLimiter(function: Callable) -> Callable:
        """
        Decorator function that limits calls to the original function.

        Args:
            function (Callable): The function to which the limit will
             be applied.

        Returns:
            Callable: The limited function.
        """

        def limit_function(*args: Any, **kwds: Any) -> None:
            """Internal function that controls the number of calls."""
            # Allows modifying the counter in the outer scope
            nonlocal count

            # Error handling to ensure the limit is not exceeded
            if count >= limit:
                print(f"Error: {repr(function)} call too many times.")
                return  # If the limit is reached, do not call the function

            count += 1  # Increment the counter
            return function(*args, **kwds)  # Call the original function

        return limit_function  # Return the limited function

    return callLimiter  # Return the decorator
