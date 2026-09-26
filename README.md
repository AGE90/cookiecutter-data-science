# Cookiecutter Data Science Template

A **Cookiecutter** template to jumpstart data science projects with a well-organized structure. This template is designed to help data scientists and machine learning practitioners create consistent and scalable project structures.

---

## Features

- **Modern Python Development**: Using [uv](https://docs.astral.sh/uv/) for fast, reproducible dependency management
- **Code Quality**: ruff (lint + format), mypy and pre-commit, passing out of the box
- **Claude Code Skill**: Scaffold a project by asking Claude, in one command, without Claude writing the files ([see below](#claude-code-skill))
- **Data Science Tools**: Incorporates popular data science libraries
- **Pipeline Stubs**: `make data`, `make features`, `make train` and `make predict` run a small working pipeline you edit for your problem
- **Development Tools**: Code quality tools and testing frameworks
- **Project Structure**: Organized directory structure for data science projects
- **Best Practices**: Follows best practices for reproducibility.
- **Extensible**: Customizable structure that can easily adapt to different workflows.

---

## Requirements

- **[uv](https://docs.astral.sh/uv/getting-started/installation/)**: runs Cookiecutter (via `uvx`), installs Python and manages the project's dependencies
- **Git** (optional, for version control)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

No separate Cookiecutter install is needed: `uvx cookiecutter ...` runs it in a throwaway environment. If you prefer, `pip install cookiecutter` works too.

---

## How to Start a New Project

### Interactive

From the folder where you want the new project:

```bash
uvx cookiecutter gh:AGE90/cookiecutter-data-science
```

Cookiecutter asks for each option (project name, author, etc.) and creates the project. The post-generation hook then pins Python, adds every dependency group with `uv add`, and initializes Git and DVC if selected.

### Non-interactive

Pass the options on the command line and skip the prompts. Any option you leave out uses its default:

```bash
uvx cookiecutter gh:AGE90/cookiecutter-data-science --no-input \
  project_name="Churn Model" \
  author_name="Jane Doe" author_email="jane@example.com" \
  use_mlflow=yes use_dvc=no
```

### Next steps

```bash
cd churn-model
make help     # list all tasks
make check    # ruff format + ruff check + mypy
make test     # pytest with coverage
```

---

## Claude Code Skill

The repo ships a [Claude Code](https://claude.com/claude-code) skill in [`skill/ds-project/SKILL.md`](skill/ds-project/SKILL.md) that lets Claude create projects from this template.

### How it works

The skill does **not** contain the template files. It tells Claude to work out the options from your request and run the single non-interactive `cookiecutter` command shown above. Cookiecutter writes the files, not Claude, so:

- **Low token cost:** Claude reads one short skill file and runs one command, instead of writing ~55 files.
- **Same result every time:** projects are identical to the ones you'd get by running Cookiecutter yourself.
- **One source of truth:** improving the template improves the skill; there is nothing to keep in sync.

Every generated project also includes a `CLAUDE.md` with the project conventions (data folders, path helpers, `uv run`, make targets), so Claude follows them when working inside the project later.

### Install

Link the skill into your personal skills folder, so it updates whenever you `git pull` this repo:

```bash
git clone https://github.com/AGE90/cookiecutter-data-science.git
ln -s "$PWD/cookiecutter-data-science/skill/ds-project" ~/.claude/skills/ds-project
```

(Or copy the folder instead of linking it.)

### Use

Start Claude Code in the folder where the project should go and ask for it, e.g.:

> Create a data science project called "Churn Model" to predict customer churn, with MLflow but no DVC. Add xgboost.

Or invoke it directly with `/ds-project`. Claude asks only for what it can't infer (usually just the name), takes your author details from `git config`, runs the command and reports the created path.

---

## Project Structure

This template provides a well-structured project layout with the following directory structure:

```text
.
├── LICENSE                <- Omitted when "No license file" is selected.
├── README.md              <- Install, pipeline, usage and structure of the project.
├── CHANGELOG.md           <- A changelog to track project updates and versions.
├── CLAUDE.md              <- Project conventions for Claude Code.
├── pyproject.toml         <- Project metadata, dependency groups and tool configuration.
├── uv.lock                <- Locked dependency versions (commit it).
├── .python-version        <- Python version pinned by uv.
├── .gitignore             <- Specifies intentionally untracked files to ignore.
├── Makefile               <- Tasks: install, pipeline (data/features/train/predict), check, test.
├── .env                   <- Environment variables (ignored by git).
├── .pre-commit-config.yaml <- Pre-commit hooks for linting/formatting.
├── app                    <- Main application code (if applicable).
│   └── main.py            <- Entry point for the application.
├── config                 <- Configuration files for the project.
├── data
│   ├── external           <- Data from third party sources.
│   ├── interim            <- Intermediate data that has been transformed.
│   ├── processed          <- The final, canonical data sets for modeling.
│   └── raw                <- The original, immutable data dump.
├── docs                   <- Project documentation (install and usage live in README.md).
│   ├── developer_guide.md <- Code style, testing, Git workflow and contributing.
│   └── code_of_conduct.md <- Code of conduct for contributors.
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
│       ├── data           <- Loading and cleaning data.
│       │   ├── data_loader.py
│       │   └── make_dataset.py    <- `make data`: data/raw -> data/interim
│       ├── features       <- Scripts to turn raw data into features for modeling.
│       │   ├── feature_engineering.py
│       │   └── build_features.py  <- `make features`: data/interim -> data/processed
│       ├── models         <- Scripts to train models and then use trained models to make predictions.
│       │   ├── model_utils.py
│       │   ├── predict_model.py   <- `make predict`: model + features -> predictions
│       │   └── train_model.py     <- `make train`: data/processed -> models/
│       ├── utils          <- Scripts to help with common tasks.
│       │   └── paths.py   <- Helper functions for relative file referencing across project.
│       └── visualization  <- Scripts to create exploratory and results oriented visualizations.
│           └── visualize.py
└── tests                  <- Test files should mirror the structure of `src`.
    ├── __init__.py
    ├── e2e/               <- End-to-end or integration tests.
    └── unit/              <- Unit tests, mirroring src structure.
        ├── test_paths.py     <- Starter tests, so `make test` passes out of the box.
        └── test_pipeline.py
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

The option `python_version` is used as the minimum Python version required for the project (`requires-python` in `pyproject.toml`), the ruff target version and the version pinned by uv in `.python-version`. It must have the format `3.X`. By default it is set to `3.12`.

### License Selection

The option `license` is used to select the license for your project. It should be one of the following options:

- `MIT`: The MIT License.
- `BSD-3-Clause`: The BSD 3-Clause License.
- `No license file`: No `LICENSE` file is created and no `license` field is set in `pyproject.toml`.

### Initialize Environment

The option `initialize_env` is used to determine whether to set up the uv environment. If selected, the post-generation hook pins the Python version, adds every dependency group below with `uv add` (creating `.venv` and `uv.lock`) and creates an empty `.env` file. Select `no` to only generate the files; you can run `make install` later.

### Project Dependencies

The option `project_dependencies` is used to specify the base project dependencies. It should be a list of Python packages separated by commas. By default its set to `[requests, pydantic, pyprojroot, python-dotenv]`. Keep `pyprojroot` and `python-dotenv`: the template code imports them.

### Extra Dependencies

The option `extra_dependencies` adds packages to the main dependencies **on top of** all the defaults, so you don't have to repeat a default list to add one library. For example, `extra_dependencies="xgboost, lightgbm"`. Empty by default.

### Development Dependencies

The option `development_dependencies` is used to specify the development dependencies. They are added to the `dev` group. By default it is set to `[mypy, ruff, pre-commit]`; keep these, since the Makefile and pre-commit hooks use them.

### Notebook Dependencies

The option `notebook_dependencies` is used to specify the notebook dependencies such as `jupyter`, `jupyterlab`, `ipywidgets`, etc. By default its set to `[ipykernel]`. `make notebook` runs Jupyter Lab on demand, so it doesn't need to be installed.

### Data Science Dependencies

The option `data_science_dependencies` is used to specify the data science dependencies such as `pandas`, `numpy`, `matplotlib`, etc. By default its set to `[pandas, numpy, openpyxl, scipy, statsmodels, scikit-learn, joblib]`. The template code uses `pandas`, `numpy`, `scikit-learn` and `joblib`, so keep them if you replace this list.

### Visualization Dependencies

The option `visualization_dependencies` is used to specify the visualization dependencies such as `seaborn`, `plotly`, `altair`, etc. By default its set to `[matplotlib, seaborn, missingno]`. `visualize.py` uses `matplotlib` and `seaborn`.

### Testing Dependencies

The option `testing_dependencies` is used to specify the testing dependencies. By default its set to `[pytest, pytest-cov, pytest-mock]`.

### Use MLFlow

The option `use_mlflow` is used to determine whether to use MLFlow for experiment tracking and model deployment. If selected, `mlflow` is added to the `data-science` group, `make train` logs each run with `log_mlflow_experiment`, and `make mlflow-ui` starts the UI. If not selected, none of the MLflow code, Make targets or docs are generated.

### Use DVC

The option `use_dvc` is used to determine whether to use DVC for data versioning and management. If selected, `dvc` is added to the `data-science` group and `dvc init` is run. `dvc init` needs a Git repository, so it only runs when `initialize_env` and `initialize_git_repository` are both `yes`. If not selected, the `dvc-*` Make targets and DVC docs are not generated.

### Initialize Git Repository

The option `initialize_git_repository` is used to determine whether to initialize a Git repository for the project. If selected, it will initialize a Git repository and commit the initial files.

---

## Contributing

Contributions are welcome! If you'd like to improve this template or add new features, feel free to submit a pull request.

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Run the template tests (they render the template with several option combinations and check the output):

    ```bash
    uvx --with cookiecutter pytest tests/
    ```

5. Submit a pull request.

---

## Support

If you encounter any issues or have questions, feel free to open an issue on the [GitHub repository](https://github.com/AGE90/cookiecutter-data-science/issues).

---
