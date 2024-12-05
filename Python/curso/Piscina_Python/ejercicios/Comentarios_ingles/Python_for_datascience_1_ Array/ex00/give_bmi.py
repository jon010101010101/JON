def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    Calculates BMI for a list of heights and weights.

    Args:
        height (list[int | float]): List of heights.
        weight (list[int | float]): List of weights.

    Returns:
        list[int | float]: List of calculated BMIs.

    Raises:
        ValueError: If the lists are empty or have different sizes.
        TypeError: If the values are not numeric or are negative.
    """
    if not height or not weight:
        raise ValueError("Height and weight lists cannot be empty.")

    if len(height) != len(weight):
        raise ValueError("Height and weight lists must have the same size.")

    bmi = []
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise TypeError("Values must be numeric.")
        if h <= 0 or w <= 0:
            raise ValueError("Values must be positive.")
        bmi.append(w / (h ** 2))
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Checks if BMI values exceed a specified limit.

    Args:
        bmi (list[int | float]): List of BMI values.
        limit (int): The limit to apply.

    Returns:
        list[bool]: List of booleans indicating if each BMI exceeds the limit.

    Raises:
        TypeError: If the limit is not a numeric value.
    """
    if not isinstance(limit, (int, float)):
        raise TypeError("The limit must be a numeric value.")

    return [b > limit for b in bmi]
