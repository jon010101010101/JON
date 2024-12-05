from load_image import ft_load
import matplotlib
matplotlib.use('TkAgg')  # Cambia el backend a TkAgg para visualización interactiva
import matplotlib.pyplot as plt


from PIL import Image
import numpy as np
import sys
import os


def print_rows_firstelem(arr, int):
    """
    Print a formatted display of the first elements
    in each row of a given array.

    Parameters:
    arr (array-like): The input array containing elements to be displayed.
    int (int): An integer specifying the display format: 0 for single brackets,
               1 for triple brackets.

    Iterates through the rows of the input array and displays the first
    elements of each row in a formatted manner. The display format is
    determined by the 'int' parameter. For 'int' equal to 0, single
    brackets are used to enclose the elements, while for 'int' equal
    to 1, triple brackets are used.
    """
    count = 0
    for row in arr:
        count += 1
    length = count
    count = 0
    for row in arr:
        if count == 0:
            if int == 1:
                print("[[[", row[0], "]", sep="")
            else:
                print("[[", row[0], sep="")
        if count > 0 and count < 3 or count > length - 4:
            if int == 1:
                if count == length - 1:
                    print("  [", row[0], "]]]", sep="")
                elif count < length - 1:
                    print("  [", row[0], "]", sep="")
            else:
                if count == length - 1:
                    print("  ", row[0], "]]", sep="")
                else:
                    print("  ", row[0], sep="")
        if count == 2:
            print("  ...")
        count += 1


def main():
    """
    Load, process, and display an image based on command-line arguments.

    This function serves as the main entry point of the script. It loads an
    image from the command-line argument, performs various image processing
    operations, and displays the resulting images. The script supports
    cropping, grayscale conversion, and zoomed image display. Errors related
    to file format and existence are caught and displayed.
    """
    try:
        path = sys.argv[1]
        if not path.lower().endswith(("jpg", "jpeg")):
            raise AssertionError("Only JPG and JPEG formats are supported.")
        if not os.path.exists(path):
            raise AssertionError("File not found:", path)
        image = Image.open(path)
        if image is None:
            raise AssertionError("Failed to load image.")

        print_rows_firstelem(ft_load(path), 0)

        zoomed_image = image.crop((400, 100, 800, 500))
        zoomed_image.save("zoomed_image.jpg")
        print(
            f"New shape after slicing: ({zoomed_image.size[0]}",
            f"{zoomed_image.size[1]}, 1) or "
            f"{zoomed_image.size})"
        )
        grayscale_image = zoomed_image.convert("L")
        print_rows_firstelem(np.array(grayscale_image), 1)

        plt.imshow(grayscale_image, cmap='gray')  # Mostrar en escala de grises
        plt.xticks(np.arange(0, 351, 50))
        plt.yticks(np.arange(0, 351, 50))
        plt.axis('on')
        plt.show()

    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()
