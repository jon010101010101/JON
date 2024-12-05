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
    # Check that lst is an iterable object
    if not isinstance(lst, range):
        raise TypeError("The argument must be of type range.")

    total = len(lst)  # Calculate the total number of elements in lst
    for i, elem in enumerate(lst):  # Use enumerate to iterate
        # over lst, obtaining both the index i (which starts at 0)
        # and the element elem in each iteration.
        yield elem  # Use yield to return the current element
        percent = (i + 1) / total * 100  # Calculate the percentage
        # completed by dividing the current index (plus 1) by the total
        # number of elements and multiplying by 100.
        bar_length = 40  # Length of the progress bar
        block = int(bar_length * percent // 100)  # Calculate how many
        # blocks of the bar should be shown based on the percentage
        # completed. The result is converted to an integer.
        bar = '█' * block + '-' * (bar_length - block)  # Create the bar
        # by concatenating filled blocks ('█') and empty blocks
        # ('-'). The number of filled blocks is equal to block, while
        # the number of empty blocks is equal to the total length
        # of the bar minus block.

        # Display the progress
        sys.stdout.write(
            f'\r{int(percent)}%|{bar:<{bar_length}}| {i + 1}/{total}'
        )

        # Print the progress on the same line using \r to
        # overwrite the previous line. It shows the percentage
        # completed, the progress bar, and how many elements have been
        # processed so far.
        sys.stdout.flush()
        # Ensures that the content is displayed immediately.
        time.sleep(0.005)  # Simulate work time

    print()  # New line at the end

    # yield is used in functions to convert them into generators
    # yield elem indicates that you want to return the value of elem in
    # each iteration of the loop, and it returns to the for loop.
