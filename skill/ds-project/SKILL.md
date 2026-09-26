---
name: ds-project
description: Scaffold a new data science / machine learning Python project (src layout, uv, ruff, mypy, pytest, optional MLflow and DVC) from the AGE90 cookiecutter template with a single command. Use when the user asks to create, start, bootstrap, or scaffold a new data science, ML, analytics, or modeling project.
---

# Scaffold a data science project

The template writes every file. Do NOT write project files yourself, and do NOT read the generated files back after it finishes. That's the point of this skill: one command instead of dozens of file writes.

## Steps

1. **Collect the answers.** Infer them from the request. Ask one short question only for what you can't infer; `project_name` is the only one that really matters. Everything else has a sensible default (table below).
   - Take the author details from `git config user.name` and `git config user.email` unless the user gave them.
   - Extra libraries the user mentions go in the matching `*_dependencies` key, **appended to the default list** (the value replaces the default, it doesn't extend it).
2. **Run one command** from the directory where the project should be created (or pass `-o <dir>`):

   ```bash
   uvx cookiecutter gh:AGE90/cookiecutter-data-science --no-input \
     project_name="Churn Model" \
     project_description="Predict customer churn" \
     author_name="..." author_email="..." \
     use_mlflow=yes use_dvc=no
   ```

   - Pass only keys that differ from the defaults. Quote every value.
   - Add `--checkout <branch>` to use a branch other than the default.
   - If the current directory is the template repo itself, use `.` instead of `gh:AGE90/cookiecutter-data-science`.
   - The post-gen hook runs `uv add` for each group, so it needs network access and takes a minute or two. Don't cancel it.
3. **Report back** in 2 or 3 lines: the created path (`./<project_slug>`), which options were on, and the next step: `cd <project_slug> && make help`.

## Options (`cookiecutter.json`)

| Key | Default | Notes |
|---|---|---|
| `project_name` | `project_name` | Human name. Slug and module are derived from it |
| `project_slug` | derived: lowercase, spaces to `-` | Directory name |
| `module_name` | derived: lowercase, spaces/`-` to `_` | Must be a valid Python identifier |
| `author_name` | `Your name` | |
| `author_email` | `you@example.com` | Must be a valid email or generation fails |
| `project_description` | `A short description of the project.` | |
| `project_url` | `https://example.com` | Must be a valid URL (scheme + host) |
| `project_version` | `0.1.0` | |
| `python_version` | `3.11` | Format `3.X` |
| `license` | `MIT` | `MIT`, `BSD-3-Clause`, `No license file` |
| `initialize_env` | `yes` | `uv add` all dependency groups. `no` = files only, nothing installed |
| `project_dependencies` | `requests, pydantic, pyprojroot, python-dotenv` | Main deps. Keep `pyprojroot` and `python-dotenv` (the template code imports them) |
| `development_dependencies` | `mypy, ruff, pre-commit` | `dev` group |
| `notebook_dependencies` | `ipykernel` | `notebook` group |
| `data_science_dependencies` | `openpyxl, scipy, statsmodels, scikit-learn, joblib` | `data-science` group |
| `visualization_dependencies` | `seaborn, missingno` | `viz` group |
| `testing_dependencies` | `pytest, pytest-cov, pytest-mock` | `test` group |
| `use_mlflow` | `yes` | Adds `mlflow` to `data-science` |
| `use_dvc` | `yes` | Adds `dvc` and runs `dvc init` (needs `initialize_env` and `initialize_git_repository` both `yes`) |
| `initialize_git_repository` | `yes` | `git init` plus an initial commit |

Dependency values are comma-separated package names, e.g. `data_science_dependencies="openpyxl, scipy, statsmodels, scikit-learn, joblib, xgboost"`.

## If it fails

- `ERROR: Invalid ...` comes from the pre-gen validation: fix that value and rerun. Nothing was created.
- Hook failure (uv, git, dvc): the files were already generated. Report the error. Don't delete the directory without asking.
- `uvx` not found: install uv (`curl -LsSf https://astral.sh/uv/install.sh | sh`) or use `pipx run cookiecutter ...`.
