from statistics import ft_statistics


def test_empty_args():
    """Test with empty arguments."""
    print("Test with empty arguments:")
    print("Input: ft_statistics(toto=\"mean\", tutu=\"median\", tata=\"quartile\")")
    ft_statistics(toto="mean", tutu="median", tata="quartile")
    print()


def test_non_numeric_args():
    """Test with non-numeric arguments."""
    print("Test with non-numeric arguments:")
    print("Input: ft_statistics(\"a\", \"b\", \"c\", toto=\"mean\", tutu=\"median\", tata=\"quartile\")")
    ft_statistics("a", "b", "c", toto="mean", tutu="median", tata="quartile")
    print()


def test_invalid_kwargs():
    """Test with invalid keyword arguments."""
    print("Test with invalid keyword arguments:")
    print("Input: ft_statistics(1, 2, 3, invalid=\"statistic\")")
    ft_statistics(1, 2, 3, invalid="statistic")
    print()


def test_insufficient_data():
    """Test with insufficient data for some calculations."""
    print("Test with insufficient data:")
    print("Input: ft_statistics(1, hello=\"std\")")
    ft_statistics(1, hello="std")  # Needs at least 2 values for std
    print()


def test_mixed_valid_invalid():
    """Test with mixed valid and invalid inputs."""
    print("Test with mixed valid and invalid inputs:")
    print("Input: ft_statistics(1, 42, \"a\", 3.14, toto=\"mean\", hello=\"world\", tutu=\"median\")")
    ft_statistics(1, 42, "a", 3.14, toto="mean", hello="world", tutu="median")
    print()


def main():
    """Main function to run error tests."""
    test_empty_args()
    test_non_numeric_args()
    test_invalid_kwargs()
    test_insufficient_data()
    test_mixed_valid_invalid()


if __name__ == "__main__":
    main()
