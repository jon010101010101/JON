from ft_calculator import calculator

if __name__ == "__main__":
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5  # Add 5 to each element
    print("---")
    
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5  # Multiply each element by 5
    print("---")
    
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5  # Subtract 5 from each element
    v3 / 5  # Divide each element by 5
