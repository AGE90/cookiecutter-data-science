"""
Pre-generation validation script for Cookiecutter.

Validates that the module name and slug adhere to Python naming conventions:
- Must start with a letter or underscore.
- Followed by letters, digits, or underscores.

Also normalizes the names and displays the derived values.

Uses Colorama for cross-platform colored output.
"""

import keyword
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

from colorama import Fore, Style, just_fix_windows_console

# --- Initialize Colorama (Windows-safe) ---
just_fix_windows_console()

# Cookiecutter variables (filled in based on user input)
PROJECT_NAME = "{{ cookiecutter.project_name }}"
PROJECT_SLUG = "{{ cookiecutter.project_slug }}"
MODULE_NAME = "{{ cookiecutter.module_name }}"
AUTHOR_EMAIL = "{{ cookiecutter.author_email }}"
PROJECT_URL = "{{ cookiecutter.project_url }}"
PYTHON_VERSION = "{{ cookiecutter.python_version }}"

# --- Constants ---
MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]*$'
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
PYTHON_VERSION_REGEX = r'^3\.(?:[0-9]|1[0-1])$'
ERROR_COLOR = Fore.RED
INFO_COLOR = Fore.CYAN
RESET_ALL = Style.RESET_ALL

# --- Helpers ---
def validate_module(name: str) -> None:
    """
    Validate module name.

    Parameters
    ----------
    name : str
        Module name to validate.
    """
    if not re.match(MODULE_REGEX, name):
        print(f"{ERROR_COLOR} ERROR: The module '{name}' is not a valid Python identifier!{RESET_ALL}")
        print(f"{INFO_COLOR} A valid module name must start with a letter or underscore and contain only letters, numbers, or underscores.{RESET_ALL}")
        sys.exit(1)
    if keyword.iskeyword(name):
        print(
            f"{ERROR_COLOR} ERROR: The module name '{name}' is a Python reserved keyword!{RESET_ALL}")
        sys.exit(1)
    print(f"{INFO_COLOR} Valid module name: {name}{RESET_ALL}")


def validate_email(email: str) -> None:
    """
    Validate email format.

    Parameters
    ----------
    email : str
        Email address to validate
    """
    if not re.match(EMAIL_REGEX, email):
        print(f"{ERROR_COLOR} ERROR: Invalid email format: {email}{RESET_ALL}")
        sys.exit(1)
    print(f"{INFO_COLOR} Valid email: {email}{RESET_ALL}")


def validate_url(url: str) -> None:
    """
    Validate URL format.

    Parameters
    ----------
    url : str
        URL to validate.

    Raises
    ------
    ValueError
        If the URL format is invalid.
    """
    try:
        result = urlparse(url)
        if not all([result.scheme, result.netloc]):
            raise ValueError("Invalid URL format")
        print(f"{INFO_COLOR} Valid URL: {url}{RESET_ALL}")
    except ValueError:
        print(f"{ERROR_COLOR} ERROR: Invalid URL format: {url}{RESET_ALL}")
        sys.exit(1)


def validate_python_version(version: str) -> None:
    """
    Validate Python version format.

    Parameters
    ----------
    version : str
        Python version to validate.
    """
    if not re.match(PYTHON_VERSION_REGEX, version):
        print(f"{ERROR_COLOR} ERROR: Invalid Python version format: {version}{RESET_ALL}")
        print(f"{INFO_COLOR} Version must be in format '3.x' where x is 0-11{RESET_ALL}")
        sys.exit(1)
    print(f"{INFO_COLOR} Valid Python version: {version}{RESET_ALL}")


# --- Main Execution ---
def main():
    """
    Validate Cookiecutter inputs.
    """
    # Validate all fields
    validate_module(MODULE_NAME)
    validate_email(AUTHOR_EMAIL)
    validate_url(PROJECT_URL)
    validate_python_version(PYTHON_VERSION)

    # Success message
    full_path = Path.cwd() / PROJECT_SLUG
    print(f"{INFO_COLOR} Project '{PROJECT_NAME}' will be created in: {full_path}{RESET_ALL}")


if __name__ == "__main__":
    main()
