# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Conventions

- Python package: `src/{{ cookiecutter.module_name }}/` (data, features, models, visualization, utils).
- Environment: uv. Run everything with `uv run <cmd>`; add deps with `uv add <pkg>` (or `uv add --group <dev|test|notebook|data-science|viz> <pkg>`). Never use pip directly.
- Paths: never hardcode. Use the helpers in `{{ cookiecutter.module_name }}.utils.paths` (`data_raw_dir("file.csv")`, `data_processed_dir(...)`, `models_dir(...)`, `reports_figures_dir(...)`, ...).
- Data flow: `data/raw` is immutable input -> `data/interim` -> `data/processed` (model-ready). Third-party data goes in `data/external`. Data files are not committed to git{% if cookiecutter.use_dvc == "yes" %}; track them with DVC (`uv run dvc add data/raw/<file>`){% endif %}.
- Notebooks in `notebooks/` are for exploration only; move reusable code into `src/`.
- Trained models go in `models/`, figures in `reports/figures/`.
- Secrets go in `.env` (git-ignored), loaded via `{{ cookiecutter.module_name }}.credentials`.
- Docstrings: numpy style. Type hints on public functions.

## Commands

- `make install`: install all dependency groups
- `make check`: ruff format + ruff check + mypy
- `make test`: pytest with coverage (tests live in `tests/unit` and `tests/e2e`)
{%- if cookiecutter.use_mlflow == "yes" %}
- `make mlflow-ui`: MLflow tracking UI
{%- endif %}
- `make help`: list every target
