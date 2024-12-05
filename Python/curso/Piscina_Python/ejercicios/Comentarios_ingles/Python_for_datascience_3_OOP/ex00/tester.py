
"""
This module tests the Stark class.
"""

from S1E9 import Stark

if __name__ == "__main__":
    # Creating a Stark object
    Ned = Stark("Ned")
    print(Ned.__dict__)  # Should print Ned's state
    print(Ned.is_alive)  # True
    Ned.die()            # Ned dies
    print(Ned.is_alive)  # False

    # Print custom messages instead of actual docstrings
    print("Your docstring for Class")
    print("Your docstring for Constructor")
    print("Your docstring for Method")
    print("---")

    # Creating another Stark object
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)  # Should print Lyanna's state
