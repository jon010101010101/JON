import sys
import antigravity
import os

def geohashing(latitude, longitude, datedow):
    """
    Calculates the geohash using the antigravity.geohash function.
    Opens the result in the browser.

    Parameters:
        latitude (float): Latitude of the location.
        longitude (float): Longitude of the location.
        datedow (str): Date and decimal value in "YYYY-MM-DD-decimal" format.
    """
    try:
        # Encode the third parameter (datedow) to bytes in UTF-8 format
        encoded_datedow = datedow.encode('utf-8')

        # Call the antigravity.geohash function with the correct parameters
        antigravity.geohash(float(latitude), float(longitude), encoded_datedow)
    except ValueError:
        print("Error: Latitude and longitude must be valid numbers.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        sys.exit(1)

def main():
    """
    Main function that manages arguments and executes the geohash calculation.
    """
    if len(sys.argv) != 4:
        print("Error: Incorrect number of arguments.")
        print("Usage: python geohashing.py <latitude> <longitude> <date-dow>")
        sys.exit(1)

    # Extract arguments from the command line
    latitude = sys.argv[1]
    longitude = sys.argv[2]
    datedow = sys.argv[3]

    # Call the geohashing function with the provided parameters
    geohashing(latitude, longitude, datedow)

if __name__ == '__main__':
    main()




# py geohashing.py 37.421542 -122.085589 2005-05-26-10458.68 2>/dev/null


