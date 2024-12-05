"""
This module tests the King class from the DiamondTrap module.
"""

from DiamondTrap import King

if __name__ == "__main__":
    # Creating a King object
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)  # Show Joffrey's state

    # Setting Joffrey's physical traits
    Joffrey.set_eyes("blue")  # Set eye color to blue
    Joffrey.set_hairs("light")  # Set hair color to light

    # Printing Joffrey's updated traits
    print(Joffrey.get_eyes())  # Print Joffrey's eye color
    print(Joffrey.get_hairs())  # Print Joffrey's hair color
    print(Joffrey.__dict__)  # Show Joffrey's updated state
