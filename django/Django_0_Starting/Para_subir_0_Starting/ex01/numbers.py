def read_and_print_numbers():
    try:
        # Open the file numbers.txt in read mode (r)
        with open('numbers.txt', 'r') as file:
            # Read the content of the file
            content = file.read()
            
            # Split the content by commas
            numbers = content.split(',')
            
            # Print each number on a separate line
            for number in numbers:
                # strip() removes whitespace at the beginning and end
                print(number.strip())
    
    except FileNotFoundError:
        print("Error: The file 'numbers.txt' was not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Call the function when the script is executed
if __name__ == '__main__':
    read_and_print_numbers()

