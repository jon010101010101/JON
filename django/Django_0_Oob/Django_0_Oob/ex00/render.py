import os
import sys

EXTENSION = ".template"
SETTINGS_FILENAME = "settings.py"

def read_file(file_path):
    """
    Reads the content of a file.

    Args:
    file_path (str): Path of the file to read.

    Returns:
    str: Content of the file.

    Raises:
    SystemExit: If an error occurs during reading.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    except PermissionError:
        print(f"Error: No permission to read {file_path}")
    except IsADirectoryError:
        print(f"Error: {file_path} is a directory")
    except Exception as e:
        print(f"Error: {e}")
    sys.exit(1)

def parse_settings(file_path):
    """
    Parses the settings file.

    Args:
    file_path (str): Path of the settings file.

    Returns:
    dict: Dictionary with configuration parameters.

    Raises:
    SystemExit: If there's an error in the file format.
    """
    content = read_file(file_path)
    param_dict = {}
    for line in content.splitlines():
        line = line.strip()
        if line and not line.startswith('#'):
            try:
                key, value = line.split('=', 1)
                param_dict[key.strip()] = value.strip().strip('"\'')
            except ValueError:
                print(f"Error: Invalid line in settings file: {line}")
                sys.exit(1)
    return param_dict

def render_template(template_path, param_dict):
    """
    Renders the template with given parameters.

    Args:
    template_path (str): Path of the template file.
    param_dict (dict): Dictionary with configuration parameters.

    Raises:
    SystemExit: If there's an error writing the output file.
    """
    content = read_file(template_path)
    rendered = content.format(**param_dict)
    
    output_path = os.path.splitext(template_path)[0] + '.html'
    try:
        with open(output_path, 'w') as f:
            f.write(rendered)
        print(f"HTML file created: {output_path}")
    except Exception as e:
        print(f"Error writing output file: {e}")
        sys.exit(1)

def main():
    """
    Main function of the program.

    Raises:
    SystemExit: If there are errors in arguments or files.
    """
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <file.template>")
        sys.exit(1)

    template_path = sys.argv[1]
    if not template_path.endswith(EXTENSION):
        print(f"Error: File must have {EXTENSION} extension")
        sys.exit(1)

    if not os.path.exists(template_path):
        print(f"Error: {template_path} does not exist")
        sys.exit(1)

    if not os.path.exists(SETTINGS_FILENAME):
        print(f"Error: {SETTINGS_FILENAME} not found")
        sys.exit(1)

    param_dict = parse_settings(SETTINGS_FILENAME)
    render_template(template_path, param_dict)

if __name__ == "__main__":
    main()







# python3 render.py myCV.template


