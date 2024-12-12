import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def cut_square(
    image: np.ndarray,
    start_height: int,
    start_width: int
) -> np.ndarray:
    """
    Cut a 400x400 square from the specified starting point of the image.

    Args:
        image (np.ndarray): The input image as a NumPy array.
        start_height (int): The starting height for the square cut.
        start_width (int): The starting width for the square cut.

    Returns:
        np.ndarray: A 400x400 square cut from the specified point of the image.

    Raises:
        ValueError: If the cut exceeds the image boundaries.
    """
    height, width, _ = image.shape
    if start_height + 400 > height or start_width + 400 > width:
        raise ValueError("Error: The cut exceeds the image boundaries.")

    return image[
        start_height:start_height + 400,
        start_width:start_width + 400
    ]


def to_grayscale(image: np.ndarray) -> np.ndarray:
    """
    Convert RGB image to grayscale.
    """
    return np.dot(image[..., :3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)


def manual_transpose(image: np.ndarray) -> np.ndarray:
    """
    Manually transpose an image (swap rows and columns).
    """
    height, width = image.shape[:2]  # Extract the height and width
    # Create a new NumPy array with inverted dimensions (width, height)
    # instead of (height, width). Iterate over each pixel and assign each
    # pixel to its transposed position by inverting the indices [j, i]
    # instead of [i, j]
    transposed_image = np.zeros((width, height), dtype=image.dtype)

    for i in range(height):
        for j in range(width):
            transposed_image[j, i] = image[i, j]

    return transposed_image


def main():
    try:
        # Load the image
        image = ft_load('animal.jpeg')

        # Adjust starting point for zooming in on a specific area (e.g., face)
        # Adjust according to the vertical position of the area of interest
        start_height = 100
        # Adjust according to the horizontal position of the area of interest
        start_width = 448

        # Cut a 400x400 square from the specified starting point
        square_image = cut_square(image, start_height, start_width)

        # Convert to grayscale
        gray_image = to_grayscale(square_image)

        # Reshape to add channel dimension
        gray_image = gray_image.reshape(400, 400, 1)

        print(
            f"The shape of image is: {gray_image.shape} "
            f"or {gray_image.shape[:2]}"
        )
        print(gray_image[:3, :3])  # Print first few pixel values

        # Manual transpose of the image
        transposed_image = manual_transpose(gray_image.squeeze())

        print(f"New shape after manual transpose: {transposed_image.shape}")
        print(transposed_image)

        # Create a figure with a specific size
        plt.figure(figsize=(4, 4))

        # Display the transposed image
        plt.imshow(transposed_image, cmap='gray', extent=[0, 400, 400, 0])

        # Set ticks and labels for axes from 0 to 350 in increments of 50
        ticks = np.arange(0, 351, 50)
        plt.xticks(ticks)
        plt.yticks(ticks)

        # Remove extra space around the plot
        plt.tight_layout()

        plt.show()

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
