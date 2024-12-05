import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """
    Calculate BMI (Body Mass Index) values based on given heights and weights.

    Args:
        height (list[int | float]): List of heights in meters.
        weight (list[int | float]): List of weights in kilograms.

    Returns:
        list[int | float]: List of calculated BMI values.

    Raises:
        ValueError: If the lists of heights and weights have different lengths.
                    If any height/weight value is less than or equal to zero.
                    If any height or weight value is not an integer or a float.
    """
    try:
        # Convert lists of heights and weights to NumPy arrays
        height_np = np.array(height, dtype=float)
        weight_np = np.array(weight, dtype=float)

        # Check if the lists have the same amount of data
        if len(height_np) != len(weight_np):
            raise TypeError("Lists(height/weight) must have the same length.")

        # Check if any values are negative
        if np.any(height_np <= 0) or np.any(weight_np <= 0):
            raise ValueError("Height and weight values must be positive.")

        # Calculate BMI
        bmi = weight_np / (height_np ** 2)

        # Return the result as a list
        return bmi.tolist()
    except Exception as error:
        print("An error occurred:", error)
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Determine whether BMI values are above a given limit.

    Args:
        bmi (list[int | float]): List of BMI values.
        limit (int): Limit to compare BMI values against.

    Returns:
        list[bool]: List of booleans indicating whether
        each BMI value is above the limit.

    Raises:
        ValueError: If any BMI value is not an integer or a float.
    """
    try:
        # Check if all BMI values are numbers
        if not all(isinstance(b, (int, float)) for b in bmi):
            raise ValueError("BMI values must be integers or floats.")

        # Apply the limit and return a list of boolean values
        return [b > limit for b in bmi]
    except ValueError as e:
        # Print an error message
        print("An error occurred:", e)
        # Return a list of False the same size as bmi
        return [False] * len(bmi)
