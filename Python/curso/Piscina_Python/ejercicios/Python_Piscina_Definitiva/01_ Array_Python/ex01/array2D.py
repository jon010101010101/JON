import sys


def slice_me(family: list, start: int, end: int) -> list:
    """
    Takes a 2D array, prints its shape, and returns a truncated version
    using the start and end parameters.

    Args:
        family: A 2D list of numbers.
        start: The starting index for slicing.
        end: The ending index for slicing.

    Returns:
        A truncated 2D list based on the start and end parameters.

    Raises:
        TypeError: If the input is not a 2D list.
        ValueError: If all rows do not have the same length.
    """
    try:
        # Check if 'family' is a valid 2D list
        if (not isinstance(family, list) or
                not all(isinstance(row, list) for row in family)):
            raise TypeError("Input must be a 2D list")

        # Check that all rows have the same length
        row_lengths = set(len(row) for row in family)
        if len(row_lengths) != 1:
            raise ValueError("All rows must have the same length")

        # Print the shape of the 2D array
        rows, cols = len(family), row_lengths.pop()
        print(f"My shape is : ({rows}, {cols})")

        # Apply slicing on the 2D array using the provided indices
        truncated = family[start:end]

        # Get the new shape of the truncated array
        new_rows, new_cols = len(truncated), cols if truncated else 0
        print(f"My new shape is : ({new_rows}, {new_cols})")

        return truncated

    except (TypeError, ValueError) as e:
        print(f"Error: {str(e)}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        sys.exit(1)
