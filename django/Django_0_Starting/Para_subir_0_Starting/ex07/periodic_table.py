import os

def parse_periodic_table(file_path):
    """Parse the periodic_table.txt file and return the element data."""
    elements = []
    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Iterate over each line in the file
        for line in file:
            # Check if the line is not empty after removing spaces
            if line.strip():
                # Split the line into name and attributes
                data = line.strip().split(' = ')
                # Get the element name
                name = data[0].strip()
                # Create a dictionary with the element's attributes
                attributes = dict(item.split(':') for item in data[1].split(', '))
                
                # Get the element's position (column), convert to integer
                column = int(attributes.get('position', '0'))
                # Get the element's atomic number, convert to integer
                atomic_number = int(attributes.get('number', '0'))

                # Determine the element's row based on its atomic number
                if atomic_number <= 2:
                    row = 1
                elif atomic_number <= 10:
                    row = 2
                elif atomic_number <= 18:
                    row = 3
                elif atomic_number <= 36:
                    row = 4
                elif atomic_number <= 54:
                    row = 5
                elif atomic_number <= 86:
                    row = 6
                else:
                    row = 7

                # Create a dictionary with the element's information
                element = {
                    "name": name,
                    "atomic_number": atomic_number,
                    "symbol": attributes.get('small', ''),
                    "atomic_mass": attributes.get('molar', ''), # ' ' default value
                    "electron": attributes.get('electron', ''),
                    "position": (row, column) # Defines the row and column
                }
                # Add the element to the list of elements
                elements.append(element)
    # Return the complete list of elements
    return elements

def generate_html(elements, output_file):
    """Generate an HTML file representing the periodic table."""
    # Start the HTML content with basic structure and CSS styles
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Periodic Table</title>
        <style>
            table { border-collapse: collapse; width: auto; }
            td { border: 1px solid black; padding: 10px; text-align: center; vertical-align: top; width: 80px; height: 80px; }
            h4 { margin: 0; }
            ul { padding-left: 20px; margin: 5px; list-style-type: none; }
            .empty { background-color: lightgray; }
        </style>
    </head>
    <body>
        <h1>Periodic Table of Elements</h1>
        <table>
    """
    # Comes from the tuple defined when creating the dictionary "position": (row, column),
    # position 0 row and position 1 column
    # Determine the maximum number of rows in the table
    max_row = max(element["position"][0] for element in elements)
    # Determine the maximum number of columns in the table
    max_column = max(element["position"][1] for element in elements)

    # Iterate over each row of the table, creates a loop from 1 to max row
    for row in range(1, max_row + 1):
        # Add an HTML tag to start a new table row
        html_content += "<tr>\n"
        # Iterate over each column of the row, creates a loop from 0 to max columns
        for column in range(0, max_column + 1):
            # Search in the elements list for the first element whose position matches
            # the current row and column. If found, assign to element. If not, None.
            element = next((el for el in elements if el["position"] == (row, column)), None)
            if element:
                # Add a cell with the element's information
                html_content += f"""
                <td>
                    <h4>{element['name']}</h4>
                    <ul>
                        <li>No {element['atomic_number']}</li>
                        <li>{element['symbol']}</li>
                        <li>{element['atomic_mass']}</li>
                        <li>{element['electron']} electrons</li>
                    </ul>
                </td>
                """
            else:
                # If there's no element, add an empty cell
                html_content += '<td class="empty"></td>\n'
        # Close the HTML row
        html_content += "</tr>\n"

    # Close the HTML structure
    html_content += """
        </table>
    </body>
    </html>
    """

    # Write the HTML content to the output file
    with open(output_file, 'w') as file:
        file.write(html_content)

def main():
    # os.path.dirname(path): Extracts the directory name from a full path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Build the full path of the input file
    input_file = os.path.join(script_dir, "periodic_table.txt")
    # Build the full path of the output file
    output_file = os.path.join(script_dir, "periodic_table.html")

    # Print a message indicating the attempt to open the file
    print(f"Attempting to open file: {os.path.basename(input_file)}")

    # Check if the input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{os.path.basename(input_file)}' not found.")
        return

    try:
        # Parse the input file to get the element data
        elements = parse_periodic_table(input_file)
        # Generate the HTML file with the periodic table
        generate_html(elements, output_file)
        # Print a success message
        print(f"Periodic table generated in HTML: {os.path.basename(output_file)}")
    except Exception as e:
        print(f"Error processing file: {e}")
        import traceback
        print(traceback.format_exc())

if __name__ == "__main__":
    main()

