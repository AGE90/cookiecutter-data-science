"""
This script handles post-project generation tasks:
1. License: Removes the empty LICENSE file when "No license file" was selected
2. uv Environment Setup: Pins Python and adds dependencies to their groups
3. Git Repository Initialization: Initializes Git repository if selected
4. Data Science Tools Setup: Configures DVC and MLflow if selected
5. Initial Commit: Commits the generated project if Git was initialized
"""

import os
import subprocess
import sys

# Keep our messages in order with subprocess output when stdout is piped
sys.stdout.reconfigure(line_buffering=True)

# Define constants for colored output (plain ANSI codes, stdlib only)
MSG_COLOR = "\033[36m"
ERROR_COLOR = "\033[31m"
RESET_ALL = "\033[0m"


# Cookiecutter variables (filled in based on user input)
LICENSE = "{{ cookiecutter.license }}"
PYTHON_VERSION = "{{ cookiecutter.python_version }}"
INITIALIZE_ENV = "{{ cookiecutter.initialize_env }}"
INITIALIZE_GIT_REPOSITORY = "{{ cookiecutter.initialize_git_repository }}"
USE_MLFLOW = "{{ cookiecutter.use_mlflow }}"
USE_DVC = "{{ cookiecutter.use_dvc }}"

# Dependency groups from cookiecutter.json
PROJECT_DEPENDENCIES = "{{ cookiecutter.project_dependencies }}"
EXTRA_DEPENDENCIES = "{{ cookiecutter.extra_dependencies }}"
DEV_DEPENDENCIES = "{{ cookiecutter.development_dependencies }}"
NOTEBOOK_DEPENDENCIES = "{{ cookiecutter.notebook_dependencies }}"
DATA_SCIENCE_DEPENDENCIES = "{{ cookiecutter.data_science_dependencies }}"
VIZ_DEPENDENCIES = "{{ cookiecutter.visualization_dependencies }}"
TEST_DEPENDENCIES = "{{ cookiecutter.testing_dependencies }}"


def run(command, error_msg):
    """
    Execute a command and exit with an error message if it fails.

    Parameters
    ----------
    command : list of str
        Command and arguments to execute.
    error_msg : str
        Message printed if the command fails.
    """
    try:
        subprocess.check_call(command)
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"{ERROR_COLOR}{error_msg}: {e}{RESET_ALL}")
        sys.exit(1)


def split_deps(dep_string):
    """Turn a comma-separated dependency string into a list of packages."""
    return [pkg.strip() for pkg in dep_string.split(",") if pkg.strip()]


# --- License ---
def remove_license():
    """Remove the empty LICENSE file when no license was selected."""
    if LICENSE == "No license file" and os.path.exists("LICENSE"):
        os.remove("LICENSE")


# --- Environment Setup ---
def add_dependencies():
    """Pin the Python version and add user-specified dependencies to each group."""
    print(f"{MSG_COLOR}Pinning Python {PYTHON_VERSION}...{RESET_ALL}")
    run(["uv", "python", "pin", PYTHON_VERSION], "Error pinning Python version")

    dep_groups = [
        (PROJECT_DEPENDENCIES, []),
        (EXTRA_DEPENDENCIES, []),
        (DEV_DEPENDENCIES, ["--group", "dev"]),
        (NOTEBOOK_DEPENDENCIES, ["--group", "notebook"]),
        (DATA_SCIENCE_DEPENDENCIES, ["--group", "data-science"]),
        (VIZ_DEPENDENCIES, ["--group", "viz"]),
        (TEST_DEPENDENCIES, ["--group", "test"]),
    ]
    if USE_MLFLOW.lower() == "yes":
        dep_groups.append(("mlflow", ["--group", "data-science"]))
    if USE_DVC.lower() == "yes":
        dep_groups.append(("dvc", ["--group", "data-science"]))

    for dep_string, group_args in dep_groups:
        pkgs = split_deps(dep_string)
        if pkgs:
            print(
                f"{MSG_COLOR}Adding dependencies: {', '.join(pkgs)} {' '.join(group_args)}{RESET_ALL}")
            run(["uv", "add"] + group_args + pkgs, "Error adding dependencies")


def create_env_file():
    """Create an .env if it doesn't already exist."""
    env_file = ".env"
    if not os.path.exists(env_file):
        print(f"{MSG_COLOR}Creating .env file...{RESET_ALL}")
        with open(env_file, "w", encoding="utf-8") as f:
            f.write("# Add your environment variables here\n")
    else:
        print(f"{MSG_COLOR}.env file already exists, skipping creation.{RESET_ALL}")


# --- Data Science Tools Setup ---
def setup_dvc():
    """Initialize DVC. Must run after `git init` (DVC requires a Git repo)."""
    print(f"{MSG_COLOR}Initializing DVC...{RESET_ALL}")
    run(["uv", "run", "dvc", "init"], "Error initializing DVC")


# --- Main Execution Logic ---
def main():
    """Main function to handle post-generation tasks based on user inputs."""
    remove_license()

    use_env = INITIALIZE_ENV.lower() == "yes"
    use_git = INITIALIZE_GIT_REPOSITORY.lower() == "yes"

    if use_env:
        add_dependencies()
        create_env_file()
    else:
        print(f"{MSG_COLOR}Skipping uv environment setup.{RESET_ALL}")

    if use_git:
        print(f"{MSG_COLOR}Initializing Git repository...{RESET_ALL}")
        run(["git", "init"], "Git command failed")

    # DVC needs both the installed package and a Git repository
    if use_env and use_git and USE_DVC.lower() == "yes":
        setup_dvc()
    elif USE_DVC.lower() == "yes":
        print(f"{MSG_COLOR}Skipping DVC init (needs uv env and Git). "
              f"Run `uv run dvc init` later.{RESET_ALL}")

    if use_git:
        run(["git", "add", "."], "Git command failed")
        run(["git", "commit", "-m", "Initial commit"], "Git command failed")

    print(f"{MSG_COLOR}All post-generation tasks completed!{RESET_ALL}")


# Run the main function
if __name__ == "__main__":
    main()
