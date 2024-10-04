"""
This script handles two optional configurations post-project generation:
1. Virtual Environment Setup: If the user opts to set up a virtual environment, this script
   creates it using the Python `venv` module and installs dependencies from `requirements.txt`.
2. Git Repository Initialization: If the user opts to initialize a Git repository, the script
   runs a series of Git commands to initialize, add, and commit files.

Colorized output is provided using the Colorama library for better readability across platforms.
"""

import os
import subprocess
import sys
from colorama import Fore, Style, just_fix_windows_console

# Initialize Colorama for Windows compatibility
just_fix_windows_console()

# Define constants for colored output
MESSAGE_COLOR = Fore.CYAN
ERROR_COLOR = Fore.RED
RESET_ALL = Style.RESET_ALL

# Cookiecutter variables (filled in based on user input)
INITIALIZE_VIRTUALENV = "{{ cookiecutter.initialize_virtualenv }}"
INITIALIZE_GIT_REPOSITORY = "{{ cookiecutter.initialize_git_repository }}"
# PYTHON_VERSION = "{{ cookiecutter.python_version }}"

# --- Virtual Environment Setup ---
def create_virtualenv():
    """Sets up a virtual environment in the project."""
    try:
        print(f"{MESSAGE_COLOR}Setting up a virtual environment...{RESET_ALL}")
        # Create virtual environment using the specified Python version
        subprocess.check_call([sys.executable, '-m', 'venv', '.venv'])
        print(f"{MESSAGE_COLOR}Virtual environment created successfully in '.venv' directory.{RESET_ALL}")
    except subprocess.CalledProcessError as e:
        print(f"{ERROR_COLOR}Error during virtual environment setup: {e}{RESET_ALL}")
        sys.exit(1)

def install_requirements():
    """Installs the required packages in the virtual environment."""
    try:
        # Determine the correct path for pip based on the OS
        if os.name == 'nt':  # Windows
            pip_executable = os.path.join('.venv', 'Scripts', 'pip')
        else:  # Unix-based systems (Linux/MacOS)
            pip_executable = os.path.join('.venv', 'bin', 'pip')

        # Check if 'requirements.txt' exists before trying to install
        if os.path.exists('requirements.txt'):
            print(f"{MESSAGE_COLOR}Installing dependencies from 'requirements.txt'...{RESET_ALL}")
            subprocess.check_call([pip_executable, 'install', '-r', 'requirements.txt'])
            print(f"{MESSAGE_COLOR}Dependencies installed successfully.{RESET_ALL}")
        else:
            print(f"{MESSAGE_COLOR}No 'requirements.txt' found. Skipping dependency installation.{RESET_ALL}")
    except subprocess.CalledProcessError as e:
        print(f"{ERROR_COLOR}Error during requirements installation: {e}{RESET_ALL}")
        sys.exit(1)

def install_project_in_editable_mode():
    """Installs the project in editable mode using pip and pyproject.toml."""
    try:
        # Determine the correct path for pip based on the OS
        if os.name == 'nt':  # Windows
            pip_executable = os.path.join('.venv', 'Scripts', 'pip')
        else:  # Unix-based systems (Linux/MacOS)
            pip_executable = os.path.join('.venv', 'bin', 'pip')

        # Check if pyproject.toml exists before installing the project
        if os.path.exists('pyproject.toml'):
            print(f"{MESSAGE_COLOR}Installing the project in editable mode with dev dependencies...{RESET_ALL}")
            subprocess.check_call([pip_executable, 'install', '-e', '.[dev]'])
            print(f"{MESSAGE_COLOR}Project installed successfully in editable mode.{RESET_ALL}")
        else:
            print(f"{MESSAGE_COLOR}No 'pyproject.toml' found. Skipping project installation in editable mode.{RESET_ALL}")
    except subprocess.CalledProcessError as e:
        print(f"{ERROR_COLOR}Error during project installation: {e}{RESET_ALL}")
        sys.exit(1)

# --- Git Repository Initialization ---
def run_git_command(command):
    """Executes a Git command using subprocess and handles errors."""
    try:
        subprocess.check_call(command)
    except subprocess.CalledProcessError as e:
        print(f"{ERROR_COLOR}ERROR: Git command '{' '.join(command)}' failed with error: {e}{RESET_ALL}")
        sys.exit(1)

def initialize_git():
    """Initializes a Git repository, adds files, and makes an initial commit."""
    print(f"{MESSAGE_COLOR}Initializing a git repository...{RESET_ALL}")

    git_commands = [
        ['git', 'init'],
        ['git', 'add', '*'],
        ['git', 'commit', '-m', 'Initial commit']
    ]

    for command in git_commands:
        run_git_command(command)

# --- Main Execution Logic ---
def main():
    """Main function to handle post-generation tasks based on user inputs."""

    # Handle virtual environment setup
    if INITIALIZE_VIRTUALENV.lower() == "yes":
        create_virtualenv()
        install_project_in_editable_mode()
        install_requirements()
    else:
        print(f"{MESSAGE_COLOR}Skipping virtual environment setup.{RESET_ALL}")

    # Handle Git repository initialization
    if INITIALIZE_GIT_REPOSITORY.lower() == "yes":
        initialize_git()
    else:
        print(f"{MESSAGE_COLOR}Skipping Git repository initialization.{RESET_ALL}")

    print(f"{MESSAGE_COLOR}All post-generation tasks completed!{RESET_ALL}")

# Run the main function
if __name__ == "__main__":
    main()
