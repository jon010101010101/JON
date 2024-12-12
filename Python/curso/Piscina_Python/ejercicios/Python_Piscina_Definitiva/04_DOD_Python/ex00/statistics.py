from typing import Any, List, Union
from math import sqrt


def mean(ls: List[Union[int, float]]) -> float:
    """Calculate the mean of a list."""
    return sum(ls) / len(ls)


def median(ls: List[Union[int, float]]) -> float:
    """Calculate the median of a list."""
    sorted_ls = sorted(ls)
    mid = len(sorted_ls) // 2
    if len(sorted_ls) % 2 != 0:
        return sorted_ls[mid]
    return (sorted_ls[mid - 1] + sorted_ls[mid]) / 2


def quartile(ls: List[Union[int, float]]) -> List[float]:
    """Calculate Quartile (25% and 75%)."""
    if len(ls) == 1:
        return [ls[0], ls[0]]

    s = sorted(ls)
    mid = len(s) // 2
    m1 = mid + 1 if len(s) % 2 else mid
    return [float(median(s[:m1])), float(median(s[mid:]))]


def var(ls: List[Union[int, float]]) -> float:
    """Calculate the variance of a list."""
    m = mean(ls)
    return sum((x - m) ** 2 for x in ls) / len(ls)


def std(ls: List[Union[int, float]]) -> float:
    """Calculate the standard deviation of a list."""
    return sqrt(var(ls))


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Calculate various statistical measures based on the provided arguments.

    Args:
        *args: Variable length argument list of numbers.
        **kwargs: Arbitrary keyword arguments specifying statistical
         operations.

    Supported operations:
        mean: Calculate the arithmetic mean of the numbers.
        median: Calculate the median value of the numbers.
        quartile: Calculate the first and third quartiles of the numbers.
        var: Calculate the variance of the numbers.
        std: Calculate the standard deviation of the numbers.

    Returns:
        None. Prints the results of specified statistical operations.

    If no valid numbers are provided, prints "ERROR" for each requested
     operation.
    If an invalid operation is requested, it is silently ignored.
    """
    # Filter valid numbers from args
    nums = [x for x in args if isinstance(x, (int, float))]

    # Define valid operations
    valid_operations = {"mean", "median", "quartile", "std", "var"}

    # Check if there are valid numbers
    if not nums:
        for _ in kwargs.values():
            print("ERROR")
        return

    # Process each requested operation in kwargs
    for operation in kwargs.values():
        if operation not in valid_operations:
            continue
        if operation == "mean":
            print(f"mean : {mean(nums)}")
        elif operation == "median":
            print(f"median : {median(nums)}")
        elif operation == "quartile":
            print(f"quartile : {quartile(nums)}")
        elif operation == "var":
            print(f"var : {var(nums)}")
        elif operation == "std":
            print(f"std : {std(nums)}")
