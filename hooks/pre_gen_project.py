"""
This script validates the Python module name provided during a Cookiecutter project
generation and ensures it adheres to standard Python naming conventions.

- A valid Python module name must:
    - Start with a letter or an underscore.
    - Be followed by any combination of letters, numbers, or underscores.
    
If the name is invalid, the script will print an error message, suggest corrections,
and exit with an error status. If valid, the script confirms success and shows the
current directory path where the project is being created.

The script uses Colorama to provide colored output, ensuring compatibility with both
Windows and Unix-based systems.
"""

import os
import re
import sys
from colorama import Fore, Style, just_fix_windows_console

# Initialize Colorama to ensure compatibility on Windows
just_fix_windows_console()

# Define constants for colorized output
ERROR_COLOR = Fore.RED
MESSAGE_COLOR = Fore.CYAN
RESET_ALL = Style.RESET_ALL

# Regex for a valid Python module name
MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

# Module name to validate
module_name = "{{ cookiecutter.module_name }}"

def validate_module_name(name):
    """Validates the Python module name using regex."""
    if not re.match(MODULE_REGEX, name):
        print(f"{ERROR_COLOR}ERROR: '{name}' is not a valid Python module name!{RESET_ALL}")
        print(f"{MESSAGE_COLOR}Please ensure the name starts with a letter or underscore and contains only letters, numbers, or underscores.{RESET_ALL}")
        sys.exit(1)  # Exit with non-zero status indicating error

def main():
    """Main function to validate the module name and print success if valid."""
    validate_module_name(module_name)
    print(f"{MESSAGE_COLOR}Well done! The module name '{module_name}' is valid.{RESET_ALL}")
    print(f"{MESSAGE_COLOR}Creating project at {os.getcwd()}{RESET_ALL}")

# Run the main function
if __name__ == "__main__":
    main()
