# {{ cookiecutter.project_name }} Installation Guide

Welcome to the **{{ cookiecutter.project_name }}** installation guide! This guide will walk you through setting up the environment, installing necessary dependencies, and configuring essential tools to ensure a smooth development experience.

---

## Prerequisites

Make sure you have the following installed before proceeding:

- **uv**: Latest version (manages Python, the virtual environment and dependencies)

To install uv, follow the [official installation guide](https://docs.astral.sh/uv/getting-started/installation/). uv installs Python {{ cookiecutter.python_version }} for you if it is missing.

---

## 1. Clone and Set Up the Project

First, clone the repository and navigate to the project directory:

```bash
git clone <repository-url>
cd {{ cookiecutter.project_slug }}
```

---

## 2. Install Dependencies with uv

uv will automatically create a virtual environment in `.venv` and install all dependencies. Run the following command in your project root:

```bash
uv sync
```

This installs every dependency group defined in `pyproject.toml` (the project sets `default-groups = "all"`), including:

- Core dependencies
- Development tools (ruff, mypy, pre-commit)
- Data science packages (pandas, scikit-learn, etc.)
- Visualization tools (matplotlib, seaborn, etc.)
- Testing frameworks (pytest, etc.)

### Optional: Install Specific Groups

You can install specific dependency groups if needed:

```bash
# Install only development dependencies
uv sync --no-default-groups --group dev

# Install data science and visualization dependencies
uv sync --no-default-groups --group data-science --group viz

# Install all groups same as 'uv sync'
uv sync --all-groups
```

---

## 3. Activate the Virtual Environment

To activate the virtual environment:

```bash
source .venv/bin/activate
```

Or run commands directly using:

```bash
uv run <command>
```

---

## 4. Set Up Development Tools

### Pre-commit Hooks (Optional)

Install pre-commit hooks:

```bash
uv run pre-commit install
```

This activates pre-commit hooks defined in .pre-commit-config.yaml for your project, ensuring code quality checks run on every commit.

### Jupyter and JupyterLab (Optional)

If you plan to use Jupyter notebooks, install the notebook group:

```bash
uv sync --no-default-groups --group notebook
```

To launch JupyterLab:

```bash
uv run --with jupyterlab jupyter lab
```

### Set Up Plotly for JupyterLab (Optional)

Install the required JupyterLab extensions for Plotly:

```bash
uv run --with jupyterlab jupyter labextension install @jupyter-widgets/jupyterlab-manager@0.36 --no-build
uv run --with jupyterlab jupyter labextension install plotlywidget@0.2.1 --no-build
uv run --with jupyterlab jupyter labextension install @jupyterlab/plotly-extension@0.16 --no-build
uv run --with jupyterlab jupyter lab build
```

---

## 5. Set Up Data Science Tools (Optional)

### Data Version Control (DVC)

If you selected DVC during project creation:

```bash
uv run dvc init
```

### MLflow

If you selected MLflow during project creation, the tracking server will be available at `http://localhost:5000`:

```bash
uv run mlflow ui
```

---

## 6. Managing Project Tasks with Make

Common tasks are defined in the `Makefile`. List them with:

```bash
make help
```

---

## 7. Testing

Run the test suite using pytest:

```bash
uv run pytest
```

For coverage reports:

```bash
uv run pytest --cov=src
```

---

---

## Final Notes

- Always use `uv run` to execute commands within the project's virtual environment
- Use `uv add <package>` to add new dependencies
- Use `uv lock --upgrade && uv sync` to update dependencies
- Check `pyproject.toml` for all available dependency groups and their purposes

You're now all set to start developing with **{{ cookiecutter.project_name }}**!
