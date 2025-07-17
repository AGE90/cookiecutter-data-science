"""
This script handles post-project generation tasks:
1. Poetry Environment Setup: Creates and configures Poetry environment with optional groups
2. Data Science Tools Setup: Configures DVC, MLflow, and Jupyter if selected
3. Git Repository Initialization: Initializes Git repository if selected
"""

import os
import subprocess
import sys
from colorama import Fore, Style, just_fix_windows_console

# Initialize Colorama for Windows compatibility
just_fix_windows_console()

# Define constants for colored output
MSG_COLOR = Fore.CYAN
ERROR_COLOR = Fore.RED
RESET_ALL = Style.RESET_ALL


# Cookiecutter variables (filled in based on user input)
INITIALIZE_POETRY_ENV = "{{ cookiecutter.initialize_poetry_env }}"
INITIALIZE_GIT_REPOSITORY = "{{ cookiecutter.initialize_git_repository }}"
USE_MLFLOW = "{{ cookiecutter.use_mlflow }}"
USE_DVC = "{{ cookiecutter.use_dvc }}"

# Dependency groups from cookiecutter.json
PROJECT_DEPENDENCIES = "{{ cookiecutter.project_dependencies }}"
DEV_DEPENDENCIES = "{{ cookiecutter.development_dependencies }}"
NOTEBOOK_DEPENDENCIES = "{{ cookiecutter.notebook_dependencies }}"
DATA_SCIENCE_DEPENDENCIES = "{{ cookiecutter.data_science_dependencies }}"
VIZ_DEPENDENCIES = "{{ cookiecutter.vizualization_dependencies }}"
TEST_DEPENDENCIES = "{{ cookiecutter.testing_dependencies }}"


# --- Environment Setup ---
def configure_poetry():
    """Configure Poetry settings."""
    print(f"{MSG_COLOR}Configuring Poetry...{RESET_ALL}")
    try:
        # Configure Poetry to create virtualenv in project directory
        subprocess.check_call(
            ["poetry", "config", "virtualenvs.in-project", "true"])
        print(f"{MSG_COLOR}Poetry configured successfully.{RESET_ALL}")
    except subprocess.CalledProcessError as e:
        print(f"{ERROR_COLOR}Error configuring Poetry: {e}{RESET_ALL}")
        sys.exit(1)


def add_dependencies():
    """Add user-specified dependencies to poetry for each group."""
    # Always include these in dev dependencies
    always_dev = {"mypy", "ruff", "black", "pre-commit"}
    # Handle dev dependencies
    dev_pkgs = {pkg.strip()
                for pkg in DEV_DEPENDENCIES.strip().split(",") if pkg.strip()}
    dev_pkgs.update(always_dev)
    dev_pkgs = sorted(dev_pkgs)
    if dev_pkgs:
        print(
            f"{MSG_COLOR}Adding dev dependencies: {', '.join(dev_pkgs)} --group dev{RESET_ALL}")
        try:
            subprocess.check_call(
                ["poetry", "add", "--group", "dev"] + dev_pkgs)
        except subprocess.CalledProcessError as e:
            print(f"{ERROR_COLOR}Error adding dev dependencies: {e}{RESET_ALL}")
            sys.exit(1)

    # Handle other groups
    dep_groups = [
        (PROJECT_DEPENDENCIES, []),
        (NOTEBOOK_DEPENDENCIES, ["--group", "notebook"]),
        (DATA_SCIENCE_DEPENDENCIES, ["--group", "data-science"]),
        (VIZ_DEPENDENCIES, ["--group", "viz"]),
        (TEST_DEPENDENCIES, ["--group", "test"]),
    ]
    for dep_string, group_args in dep_groups:
        dep_string = dep_string.strip()
        if dep_string:
            pkgs = [pkg.strip()
                    for pkg in dep_string.split(",") if pkg.strip()]
            if pkgs:
                print(
                    f"{MSG_COLOR}Adding dependencies: {', '.join(pkgs)} {' '.join(group_args)}{RESET_ALL}")
                try:
                    subprocess.check_call(
                        ["poetry", "add"] + group_args + pkgs)
                except subprocess.CalledProcessError as e:
                    print(f"{ERROR_COLOR}Error adding dependencies: {e}{RESET_ALL}")
                    sys.exit(1)


def create_env_file():
    """Create an .env if it doesn't already exist."""
    env_file = ".env"
    if not os.path.exists(env_file):
        print(f"{MSG_COLOR}Creating .env file...{RESET_ALL}")
        with open(env_file, "w", encoding="utf-8") as f:
            f.write("# Add your environment variables here\n")
        print(f"{MSG_COLOR}.env file created successfully.{RESET_ALL}")
    else:
        print(f"{MSG_COLOR}.env file already exists, skipping creation.{RESET_ALL}")


# --- Data Science Tools Setup ---
def setup_mlflow():
    """Configure MLflow if selected."""
    print(f"{MSG_COLOR}Setting up MLflow...{RESET_ALL}")
    try:
        subprocess.check_call(["poetry", "add"] +
                              ["--group", "data-science", "mlflow"])
        os.makedirs("models/mlruns", exist_ok=True)
        print(f"{MSG_COLOR}MLflow directory created successfully.{RESET_ALL}")
    except subprocess.CalledProcessError as e:
        print(f"{ERROR_COLOR}Error setting up MLflow: {e}{RESET_ALL}")
        sys.exit(1)


def setup_dvc():
    """Initialize DVC if selected."""
    print(f"{MSG_COLOR}Setting up DVC...{RESET_ALL}")
    try:
        subprocess.check_call(["poetry", "add"] +
                              ["--group", "data-science", "dvc"])
        # Initialize DVC repository
        subprocess.check_call(["dvc", "init"])
        # Create default .dvc directories
        os.makedirs("data/raw", exist_ok=True)
        os.makedirs("data/processed", exist_ok=True)
        os.makedirs("data/external", exist_ok=True)
        print(f"{MSG_COLOR}DVC initialized successfully.{RESET_ALL}")
    except subprocess.CalledProcessError as e:
        print(f"{ERROR_COLOR}Error initializing DVC: {e}{RESET_ALL}")
        sys.exit(1)


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
    print(f"{MSG_COLOR}Initializing Git repository...{RESET_ALL}")
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
    if INITIALIZE_POETRY_ENV.lower() == "yes":
        configure_poetry()
        add_dependencies()
        create_env_file()
    else:
        print(f"{MSG_COLOR}Skipping virtual environment setup.{RESET_ALL}")

    # Handle data science tools setup
    if USE_MLFLOW.lower() == "yes":
        setup_mlflow()

    if USE_DVC.lower() == "yes":
        setup_dvc()

    # Handle Git repository initialization
    if INITIALIZE_GIT_REPOSITORY.lower() == "yes":
        initialize_git()
    else:
        print(f"{MSG_COLOR}Skipping Git repository initialization.{RESET_ALL}")

    print(f"{MSG_COLOR}All post-generation tasks completed!{RESET_ALL}")


# Run the main function
if __name__ == "__main__":
    main()
