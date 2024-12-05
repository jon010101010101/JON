def ft_filter(func, iterable):
    """
    Filters the elements of the iterable according to the provided function.

    Args:
        func: Function that determines if an element should be included.
        iterable: Iterable to filter.

    Returns:
        List of elements that meet the condition.
    """
    return [item for item in iterable if func(item)]
