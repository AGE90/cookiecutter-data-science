# Cookiecutter Data Science Template

A **Cookiecutter** template to jumpstart data science projects with a well-organized structure. This template is designed to help data scientists and machine learning practitioners create consistent and scalable project structures.

---

## Features

- **Modern Python Development**: Using Poetry for dependency management
- **Data Science Tools**: Incorporates popular data science libraries
- **Development Tools**: Code quality tools and testing frameworks
- **Project Structure**: Organized directory structure for data science projects
- **Best Practices**: Follows best practices for reproducibility.
- **Extensible**: Customizable structure that can easily adapt to different workflows.

---

## Requirements

Before using the Cookiecutter template, ensure you have the following installed in your system:

- **Python 3.9+**
- **[Cookiecutter Python package](https://cookiecutter.readthedocs.io/en/latest/installation.html)**
- **Poetry**: For dependency management and packaging
- **Git** (optional, for version control)

You can install the Cookiecutter package via `pip`:

```bash
pip install cookiecutter
```

It is also recommended to have **Poetry** installed for managing project dependencies. You can install Poetry by following the instructions on the [Poetry website](https://python-poetry.org/docs/#installation).

---

## How to Start a New Project

1. **Navigate to the folder** where you want to create your new project.

2. **Run Cookiecutter** with the following command to generate a new project from this template:

    ```bash
    cookiecutter https://github.com/AGE90/-cookiecutter-data-science
    ```

3. **Follow the prompts**: Cookiecutter will ask you a series of questions (e.g., project name, author, etc.) and create a customized project structure based on your responses.

---

## Project Structure

This template provides a well-structured project layout with the following directory structure:

```text
.
├── LICENSE
├── README.md              <- The top-level README for developers using this project.
├── CHANGELOG.md           <- A changelog to track project updates and versions.
├── pyproject.toml         <- Project configuration file (replaces setup.py and requirements.txt).
├── .gitignore             <- Specifies intentionally untracked files to ignore.
├── Makefile               <- Automate common tasks like testing, running, or setting up.
├── .env                   <- Environment variables (ignored by git).
├── .pre-commit-config.yaml <- Pre-commit hooks for linting/formatting.
├── app                    <- Main application code (if applicable).
│   └── main.py            <- Entry point for the application.
├── config                 <- Configuration files for the project.
│   ├── dev.yml            <- Development environment configuration.
│   └── prod.yml           <- Production environment configuration.
├── data
│   ├── external           <- Data from third party sources.
│   ├── interim            <- Intermediate data that has been transformed.
│   ├── processed          <- The final, canonical data sets for modeling.
│   └── raw                <- The original, immutable data dump.
├── docs                   <- Project documentation.
│   ├── project_structure.md    <- Project structure tree.
│   ├── install.md         <- Detailed instructions to set up this project.
│   ├── api.md             <- API documentation.
│   ├── user_guide.md      <- User guide for the project.
│   ├── developer_guide.md <- Guide for developers contributing to the project.
│   ├── code_of_conduct.md <- Code of conduct for contributors.
│   └── contributing.md    <- Guidelines for contributing to the project.
├── logs                   <- Log files.
├── models                 <- Trained and serialized models, model predictions, or model summaries.
├── notebooks              <- Jupyter notebooks. Naming convention is a number (for ordering),
│                             the creator's initials, and a short `-` delimited description, e.g.
│                             `01-AGE90-initial_data_exploration`.
├── references             <- Data dictionaries, manuals, and all other explanatory materials.
├── reports                <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures            <- Generated graphics and figures to be used in reporting.
├── scripts                <- Utility scripts for project management, data processing, etc.
│   ├── data_download.sh   <- Script to download raw data.
│   └── setup_env.sh       <- Script to set up the development environment.
├── src
│   └── {{ cookiecutter.module_name }}  <- Source code for use in this project.
│       ├── __init__.py    <- Makes {{ cookiecutter.module_name }} a Python module.
│       ├── __main__.py    <- Main entry point for the module.
│       ├── credentials.py <- Credentials builder for the project.
│       ├── data           <- Scripts to download or generate data.
│       │   ├── data_loader.py
│       │   └── make_dataset.py
│       ├── features       <- Scripts to turn raw data into features for modeling.
│       │   ├── feature_enineering.py
│       │   └── build_features.py
│       ├── models         <- Scripts to train models and then use trained models to make predictions.
│       │   ├── model_utils.py
│       │   ├── predict_model.py
│       │   └── train_model.py
│       ├── utils          <- Scripts to help with common tasks.
│       │   └── paths.py   <- Helper functions for relative file referencing across project.
│       └── visualization  <- Scripts to create exploratory and results oriented visualizations.
│           └── visualize.py
└── tests                  <- Test files should mirror the structure of `src`.
    ├── __init__.py
    ├── conftest.py        <- Shared pytest fixtures.
    ├── e2e/               <- End-to-end or integration tests.
    └── unit/              <- Unit tests, mirroring src structure.
```

---

## Project Setup Options

### Project Name

The option `project_name` is used as the main title in the README.md file. Consider using a descriptive name that reflects the purpose of the project. For example, "Data Science Project: Customer Segmentation."

### Project Slug

The option `project_slug` is used as the main directory name. It should be lowercase and use hyphens (- or _) instead of spaces. For example, "data-science-project."

### Module Name

The option `module_name` is used as the name of the main source code directory. It should be a valid Python package name, typically lowercase and without spaces. For example, "customer_segmentation".

### Author Name

The option `author_name` is used as the author's name in the `pyproject.toml` file. It should be your full name or a pseudonym. For example, "John Doe".

### Author Email

The option `author_email` is used as the author's email in the `pyproject.toml` file. It should be a valid email address. For example, "<john.doe@example.com>".

### Project Description

The option `project_description` is used as the project description in the `pyproject.toml` file. It should be a brief summary of the project's purpose and goals. For example, "A data science project focused on customer segmentation."

### Project URL

The option `project_url` is used as the project URL in the `pyproject.toml` file. It should be the URL of the project's repository or website. For example, "<https://github.com/johndoe/data-science-project>".

### Project Version

The option `project_version` is used as the initial version of the project in the `pyproject.toml` file. It should follow semantic versioning (e.g., "0.1.0") where the first number represents the major version, the second the minor version, and the third the patch version.

### Python Version

The option `python_version` is used as the minimum Python version required for the project in the `pyproject.toml` file. It should be a valid Python version number (e.g., "3.11").

### License Selection

The option `license_selection` is used to select the license for your project. It should be one of the following options:

- `MIT`: The MIT License.
- `BSD-3-Clause`: The BSD 3-Clause License.
- No licence file: If you do not want to include a license file, select "No licence file".

### Initialize Poetry Environment

The option `initialize_poetry_env` is used to determine whether to initialize a Poetry environment for the project. If selected, it will create a virtual environment and set up the project with Poetry.

### Project Dependencies

The option `project_dependencies` is used to specify the base project dependencies. It should be a list of Python packages separated by commas. For example, "pandas, numpy, matplotlib". By default its set to `[requests, pydantic, pyprojroot, python-dotenv]`.

### Development Dependencies

The option `development_dependencies` is used to specify the development dependencies. The packages `[mypy, ruff, black, pre-commit]` are always included. You can add more if you want by entering a list of Python packages separated by commas.

### Notebook Dependencies

The option `notebook_dependencies` is used to specify the notebook dependencies such as `jupyter`, `jupyterlab`, `ipywidgets`, etc. By default its set to `[ipywidgets]`.

### Data Science Dependencies

The option `data_science_dependencies` is used to specify the data science dependencies such as `pandas`, `numpy`, `matplotlib`, etc. By default its set to `["openpyxl, scipy, statsmodels, scikit-learn, joblib"]`.

### Visualization Dependencies

The option `visualization_dependencies` is used to specify the visualization dependencies such as `seaborn`, `plotly`, `altair`, etc. By default its set to `[seaborn, missingno]`.

### Testing Dependencies

The option `testing_dependencies` is used to specify the testing dependencies. By default its set to `[pytest, pytest-cov, pytest-mock]`.

### Use MLFlow

The option `use_mlflow` is used to determine whether to use MLFlow for experiment tracking and model deployment. If selected, it will install the necessary dependencies and configure MLFlow for your project.

### Use DVC

The option `use_dvc` is used to determine whether to use DVC for data versioning and management. If selected, it will install the necessary dependencies and configure DVC for your project.

### Initialize Git Repository

The option `initialize_git_repo` is used to determine whether to initialize a Git repository for the project. If selected, it will initialize a Git repository and commit the initial files.

---

## Contributing

Contributions are welcome! If you'd like to improve this template or add new features, feel free to submit a pull request.

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Submit a pull request.

---

## Support

If you encounter any issues or have questions, feel free to open an issue on the [GitHub repository](https://github.com/AGE90/-cookiecutter-data-science/issues).

---
