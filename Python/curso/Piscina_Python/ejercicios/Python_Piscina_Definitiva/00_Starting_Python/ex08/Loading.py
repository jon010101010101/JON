# The function must copy the function tqdm with the yield operator

import sys
import time

"""
Definition of ft_tqdm:

    The function takes a range as an argument and uses a for loop to
    iterate over the elements. This function does not return anything (None).

    Enumerate is used to obtain both the index (i) and the element (elem).
    We calculate the percentage completed and build a visual progress bar.
    We use sys.stdout.write and sys.stdout.flush to update the same line
    in the console and display the progress.
"""


def ft_tqdm(lst: range) -> None:
    if not isinstance(lst, range):
        raise TypeError("The argument must be of type range.")

    total = len(lst)
    for i, elem in enumerate(lst):
        yield elem
        percent = (i + 1) / total * 100
        bar_length = 160
        block = int(bar_length * percent // 100)
        bar = '█' * block + '-' * (bar_length - block)
        sys.stdout.write(
            f'\r{int(percent)}%|{bar:<{bar_length}}| {i + 1}/{total}'
        )
        sys.stdout.flush()
        time.sleep(0.005)

    print()
