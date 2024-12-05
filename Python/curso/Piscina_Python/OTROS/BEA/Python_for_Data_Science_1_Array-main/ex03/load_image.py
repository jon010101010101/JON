from PIL import Image
import numpy as np
import os


def ft_load(path: str) -> np.ndarray:
    """
    Load an image from the specified path and return it as a NumPy array.

    Parameters:
    path (str): The path to the image file to be loaded.

    Returns:
    np.ndarray: A NumPy array representing the loaded image.

    Raises:
    AssertionError: If the image format is wrong or the file is not found.

    Loads an image from the given path and performs checks to ensure
    compatibility and validity. Only JPG and JPEG formats are supported. If the
    file does not exist or the format is not supported, an Error is raised.
    The image is then converted to a NumPy array and its shape is printed.
    """
    try:
        if not path.lower().endswith(("jpg", "jpeg")):
            raise AssertionError("Only JPG and JPEG formats are supported.")
        if not os.path.exists(path):
            raise AssertionError(f"File not found: {path}")
        img = Image.open(path)
        print(
            f"The shape of image is: "
            f"({img.size[1]}, {img.size[0]}, {len(img.getbands())})"
        )
        return np.array(img)
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
import matplotlib
matplotlib.use('Qt5Agg')  # Cambia el backend a Qt5Agg
import matplotlib.pyplot as plt
import numpy as np
import cv2

def main():
    image_path = 'animal.jpeg'
    original_image = cv2.imread(image_path)
    print("The shape of image is:", original_image.shape)

    resized_image = cv2.resize(original_image, (400, 400))
    print(resized_image)

    # Convertir la imagen a escala de grises
    grayscale_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    print("New shape after slicing:", grayscale_image.shape, "or", (grayscale_image.shape[0], grayscale_image.shape[1]))
    print(grayscale_image)

    # Mostrar la imagen en una ventana
    plt.imshow(grayscale_image, cmap='gray')  # Mostrar en escala de grises
    plt.show()

if __name__ == "__main__":
    main()