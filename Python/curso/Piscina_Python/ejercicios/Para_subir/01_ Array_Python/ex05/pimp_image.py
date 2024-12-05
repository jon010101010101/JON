import numpy as np
import matplotlib.pyplot as plt  # Import for visualization


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the colors of the received image.

    Args:
        array (np.ndarray): The input image array.

    Returns:
        np.ndarray: The inverted image array.
    """
    inverted = 255 - array  # Inversion of colors
    display_image(inverted, "Inverted Image")
    return inverted


def ft_red(array: np.ndarray) -> np.ndarray:
    """Keeps the red channel of the image, setting others to zero.

    Args:
        array (np.ndarray): The input image array.

    Returns:
        np.ndarray: The red-filtered image array.
    """
    # Create a copy to avoid modifying the original
    red_array = np.copy(array)
    red_array[:, :, 1] = 0  # Set the green channel to 0
    red_array[:, :, 2] = 0  # Set the blue channel to 0
    display_image(red_array, "Red Filtered Image")
    return red_array


def ft_green(array: np.ndarray) -> np.ndarray:
    """Keeps the green channel of the image, setting others to zero.

    Args:
        array (np.ndarray): The input image array.

    Returns:
        np.ndarray: The green-filtered image array.
    """
    # Create a copy to avoid modifying the original
    green_array = np.copy(array)
    green_array[:, :, 0] = 0  # Set the red channel to 0
    green_array[:, :, 2] = 0  # Set the blue channel to 0
    display_image(green_array, "Green Filtered Image")
    return green_array


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Keeps the blue channel of the image, setting others to zero.

    Args:
        array (np.ndarray): The input image array.

    Returns:
        np.ndarray: The blue-filtered image array.
    """
    # Create a copy to avoid modifying the original
    blue_array = np.copy(array)
    blue_array[:, :, 0] = 0  # Set the red channel to 0
    blue_array[:, :, 1] = 0  # Set the green channel to 0
    display_image(blue_array, "Blue Filtered Image")
    return blue_array


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Converts the image to grayscale by averaging basic colors.

    Args:
        array (np.ndarray): The input image array.

    Returns:
        np.ndarray: The grayscale image array.
    """
    # Calculate the mean
    grey_array = np.mean(array, axis=2).astype(np.uint8)
    grey_image = np.stack((grey_array,) * 3, axis=-1)

    display_image(grey_image, "Grayscale Image")

    return grey_image


def display_image(image, title):
    """Displays a single image in a plot.

    Args:
        image (np.ndarray): The image to display.
        title (str): The title for the plot.
    """
    plt.imshow(image)
    plt.title(title)
    plt.axis('off')
    plt.show()  # Show the single filtered image
