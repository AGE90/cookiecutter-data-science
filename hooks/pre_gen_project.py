"""
Pre-generation validation script for Cookiecutter.

Validates that the module name and slug adhere to Python naming conventions:
- Must start with a letter or underscore.
- Followed by letters, digits, or underscores.

Also normalizes the names and displays the derived values.

Uses Colorama for cross-platform colored output.
"""

import os
import re
import sys
from colorama import Fore, Style, just_fix_windows_console

# --- Initialize Colorama (Windows-safe) ---
just_fix_windows_console()

# --- Constants ---
MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]*$'
ERROR_COLOR = Fore.RED
INFO_COLOR = Fore.CYAN
RESET_ALL = Style.RESET_ALL

# --- Helpers ---
def normalize_name(name):
    """Normalize a name by lowercasing and replacing hyphens/spaces with underscores."""
    return re.sub(r'[-\s]+', '_', name.strip().lower())

def validate_identifier(name, label):
    """Validate a Python identifier using regex."""
    if not re.match(MODULE_REGEX, name):
        print(f"{ERROR_COLOR}❌ ERROR: The {label} '{name}' is not a valid Python identifier!{RESET_ALL}")
        print(f"{INFO_COLOR}⚠ A valid {label} must start with a letter or underscore and contain only letters, numbers, or underscores.{RESET_ALL}")
        sys.exit(1)
    print(f"{INFO_COLOR}✅ Valid {label}: {name}{RESET_ALL}")

def is_placeholder(value, keywords):
    """Check if a value is a placeholder."""
    return not value or any(k in value.lower() for k in keywords)

# --- Main Execution ---
def main():
    """
    Validate Cookiecutter inputs and normalize values.
    """
    # Get Cookiecutter values (they are string-rendered here)
    raw_project_name = "{{ cookiecutter.project_name }}"
    raw_slug = "{{ cookiecutter.project_slug }}"
    raw_module_name = "{{ cookiecutter.module_name }}"
    
    # Check for placeholder-like input
    if is_placeholder(raw_slug, ["project_slug", "slug"]):
        print(f"{ERROR_COLOR}❌ ERROR: Please specify a valid project slug.{RESET_ALL}")
        sys.exit(1)
    if is_placeholder(raw_module_name, ["module_name", "module"]):
        print(f"{ERROR_COLOR}❌ ERROR: Please specify a valid module name.{RESET_ALL}")
        sys.exit(1)

    # Normalize values
    slug = normalize_name(raw_slug)
    module_name = normalize_name(raw_module_name)
    
    print(f"{INFO_COLOR}🔧 Normalized slug: {slug}{RESET_ALL}")
    print(f"{INFO_COLOR}🔧 Normalized module name: {module_name}{RESET_ALL}")

    # Validate both
    validate_identifier(slug, "project slug")
    validate_identifier(module_name, "module name")

    # Success message
    print(f"{INFO_COLOR}📁 Project {raw_project_name} will be created in: {os.getcwd()}{RESET_ALL}")

if __name__ == "__main__":
    main()
