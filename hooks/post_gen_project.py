"""
This script initializes a Git repository if the user has opted to do so during
Cookiecutter project generation.

- It checks the `initialize_git_repository` flag.
- If 'Yes', the script runs the following Git commands:
    - `git init` to initialize the repository.
    - `git add *` to add all files to the staging area.
    - `git commit -m "Initial commit"` to create the first commit.
    
The script uses Colorama to ensure colorized output works on both Windows and Unix-based systems.
"""

import sys
import subprocess
from colorama import Fore, Style, just_fix_windows_console

# Initialize Colorama for Windows compatibility
just_fix_windows_console()

# Define constants for colored output
MESSAGE_COLOR = Fore.CYAN
RESET_ALL = Style.RESET_ALL

# User input from Cookiecutter to determine whether to initialize a Git repository
initialize_git_repository = "{{ cookiecutter.initialize_git_repository }}"


def run_git_command(command):
    """Executes a Git command using subprocess and handles errors."""
    try:
        subprocess.check_call(command)
    except subprocess.CalledProcessError as e:
        print(
            f"{Fore.RED}ERROR: Git command '{' '.join(command)}' failed with error: {e}{RESET_ALL}")
        sys.exit(1)  # Exit with non-zero code to indicate failure


def initialize_git():
    """Initializes a Git repository, adds files, and makes an initial commit."""
    print(f"{MESSAGE_COLOR}Initializing a git repository...{RESET_ALL}")

    # List of Git commands to run
    git_commands = [
        ['git', 'init'],
        ['git', 'add', '*'],
        ['git', 'commit', '-m', 'Initial commit']
    ]

    # Run each command and handle potential errors
    for command in git_commands:
        run_git_command(command)


def main():
    """Main function to check the flag and initialize the Git repository if needed."""
    if initialize_git_repository.lower() == 'yes':
        initialize_git()

    print(f"{MESSAGE_COLOR}All set!{RESET_ALL}")


# Run the main function
if __name__ == "__main__":
    main()
