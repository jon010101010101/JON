import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load  # Import the image loading function


def cut_square(
    image: np.ndarray,
    start_height: int,
    start_width: int,
    size: int = 400
) -> np.ndarray:
    height, width, _ = image.shape
    if start_height + size > height or start_width + size > width:
        raise ValueError("The cut exceeds the image boundaries.")

    cropped_image = image[
        start_height:start_height + size,
        start_width:start_width + size
    ]
    return cropped_image


def to_grayscale(image: np.ndarray) -> np.ndarray:
    return np.dot(image[..., :3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)


def display_zoomed_image(image: np.ndarray):
    """
    Displays the image with scales on x and y axes.

    Args:
        image (np.ndarray): The input image array.
    """
    plt.figure(figsize=(5, 5))
    # squeeze to remove unnecessary dimensions
    plt.imshow(image.squeeze(), cmap='gray')

    # Add scales on x and y axis
    plt.xlabel("")
    plt.ylabel("")

    # Show tick marks
    plt.xticks(range(0, image.shape[1], 50))
    plt.yticks(range(0, image.shape[0], 50))

    plt.grid(False)
    plt.axis('on')  # Show axis
    plt.title("")
    plt.show()


def main():
    # Specify the path to the image directly here
    image_path = 'animal.jpeg'

    try:
        # Load the image using the function from load_image.py
        image = ft_load(image_path)

        # Process the image
        start_height = 100
        start_width = 450

        square_image = cut_square(image, start_height, start_width)
        gray_image = to_grayscale(square_image)

        # Reshape for display purposes
        gray_image = gray_image.reshape(400, 400, 1)

        print(
            f"New shape after slicing: {gray_image.shape} "
            f"or {gray_image.shape[:2]}"
        )
        # Print first 3x3 pixels of the grayscale image
        print(gray_image[:3, :3])

        # Display the zoomed grayscale image
        display_zoomed_image(gray_image)

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
