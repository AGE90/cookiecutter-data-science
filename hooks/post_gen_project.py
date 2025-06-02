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
import shutil
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
def install_poetry_env():
    """Install dependencies using Poetry and all groups."""
    print(f"{MESSAGE_COLOR}Installing dependencies with Poetry...{RESET_ALL}")
    try:
        subprocess.check_call(["poetry", "install", "--with", "dev,test,notebook,data-science,viz"])
        print(f"{MESSAGE_COLOR}Poetry environment set up successfully.{RESET_ALL}")
    except subprocess.CalledProcessError as e:
        print(f"{ERROR_COLOR}Error installing dependencies: {e}{RESET_ALL}")
        sys.exit(1)

def copy_env_file():
    """Copy .env.example to .env if it doesn't already exist."""
    src = ".env.example"
    dst = ".env"
    if os.path.exists(src):
        if not os.path.exists(dst):
            shutil.copyfile(src, dst)
            print(f"{MESSAGE_COLOR}Copied '{src}' to '{dst}'.{RESET_ALL}")
        else:
            print(f"{MESSAGE_COLOR}'{dst}' already exists. Skipping copy.{RESET_ALL}")
    else:
        print(f"{ERROR_COLOR}No '{src}' found to copy.{RESET_ALL}")

# --- Git Repository Initialization ---
def run_git_command(command):
    """Execute a Git command and handle errors."""
    try:
        subprocess.check_call(command)
    except subprocess.CalledProcessError as e:
        print(f"{ERROR_COLOR}Git command failed: {' '.join(command)}\n{e}{RESET_ALL}")
        sys.exit(1)

def initialize_git():
    """Initialize a Git repository."""
    print(f"{MESSAGE_COLOR}Initializing Git repository...{RESET_ALL}")
    git_commands = [
        ['git', 'init'],
        ['git', 'add', '.'],
        ['git', 'commit', '-m', 'Initial commit'],
    ]
    for cmd in git_commands:
        run_git_command(cmd)

# --- Main Execution Logic ---
def main():
    """Main function to handle post-generation tasks based on user inputs."""

    # Handle virtual environment setup
    if INITIALIZE_VIRTUALENV.lower() == "yes":
        install_poetry_env()
        copy_env_file()
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
