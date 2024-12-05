from functools import wraps
from typing import Any


def callLimit(limit: int):
    """
    Takes a 'limit' to restrict times a decorated funct. can be called.

    Parameters:
    limit (int): Number of times the function can be called.

    Returns:
    function: A decorator that restricts the number of times
    a function can be called.
    """
    count = 0

    def callLimiter(function):
        """object to return wrapped function"""

        @wraps(function)
        def limit_function(*args: Any, **kwds: Any):
            """
            wrapped function with limiting logic.If it is over the limit,
            is raised an error.
            """
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")
                return
        return limit_function

    return callLimiter
