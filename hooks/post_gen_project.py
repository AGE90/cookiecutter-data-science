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
initialize_virtualenv = "{{ cookiecutter.initialize_virtualenv }}"
initialize_git_repository = "{{ cookiecutter.initialize_git_repository }}"
python_version = "{{ cookiecutter.python_version }}"

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
        if os.path.exists('requirements.txt'):
            print(f"{MESSAGE_COLOR}Installing dependencies from 'requirements.txt'...{RESET_ALL}")
            subprocess.check_call(['.venv/bin/pip', 'install', '-r', 'requirements.txt'])
            print(f"{MESSAGE_COLOR}Dependencies installed successfully.{RESET_ALL}")
        else:
            print(f"{MESSAGE_COLOR}No 'requirements.txt' found. Skipping dependency installation.{RESET_ALL}")
    except subprocess.CalledProcessError as e:
        print(f"{ERROR_COLOR}Error during requirements installation: {e}{RESET_ALL}")
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
    if initialize_virtualenv.lower() == "yes":
        create_virtualenv()
        install_requirements()
    else:
        print(f"{MESSAGE_COLOR}Skipping virtual environment setup.{RESET_ALL}")
    
    # Handle Git repository initialization
    if initialize_git_repository.lower() == "yes":
        initialize_git()
    else:
        print(f"{MESSAGE_COLOR}Skipping Git repository initialization.{RESET_ALL}")

    print(f"{MESSAGE_COLOR}All post-generation tasks completed!{RESET_ALL}")

# Run the main function
if __name__ == "__main__":
    main()
