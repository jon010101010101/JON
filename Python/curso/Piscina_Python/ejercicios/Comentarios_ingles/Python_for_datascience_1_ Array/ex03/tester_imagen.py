
from PIL import Image  # Import the PIL library for image manipulation
import numpy as np  # Import numpy for working with arrays

def ft_load(path: str) -> np.ndarray:
    """
    Loads an image, prints its shape and pixel content in RGB format.

    Parameters:
    path (str): The path to the image file.

    Returns:
    np.ndarray: The pixel data of the image in RGB format.

    Exceptions:
    ValueError: If the image format is not supported or if there is an issue loading the image.
    """
    try:
        # Load the image
        image = Image.open(path)
        
        # Ensure the image is in RGB format
        image = image.convert('RGB')
        
        # Convert the image to a numpy array
        pixels = np.array(image)
        
        # Print the shape of the image (dimensions and color channels)
        print(f"The shape of the image is: {pixels.shape}")
        
        return pixels  # Return the pixel data in RGB format
    
    except IOError:
        # If there is an error loading the image, raise a ValueError
        raise ValueError(f"Error: Cannot load the image at '{path}'. Please check the path and file format.")
    except Exception as e:
        # For any other unexpected error, also raise a ValueError
        raise ValueError(f"An unexpected error occurred: {e}")

def display_image(pixels: np.ndarray):
    """
    Displays the image from the pixel data.

    Parameters:
    pixels (np.ndarray): The pixel data in RGB format.
    """
    image = Image.fromarray(pixels.astype('uint8'), 'RGB')
    image.show()  # Show the image

if __name__ == "__main__":  # Check if this file is being run directly
    try:
        # Call the ft_load function and store the pixels in the variable
        pixels = ft_load("landscape.jpg")  # Make sure the image is in the same directory
        print(pixels)  # Print the pixel content

        # Display the image on the screen
        display_image(pixels)
    except ValueError as e:
        # If a ValueError occurs, print it
        print(e)
