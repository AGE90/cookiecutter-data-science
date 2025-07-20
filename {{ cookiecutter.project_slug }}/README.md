# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

---

## Project Overview

<!-- Add a brief overview of the project here. -->

---

## Installation Steps

Please read [install.md](docs/install.md) for details on how to set up this project.

---

## Key Features

- **Dependency Management**: Using Poetry for reliable dependency management
- **Data Version Control**: Optional DVC integration for data versioning
- **ML Experiment Tracking**: Optional MLflow integration for experiment tracking
- **Interactive Dashboards**: Optional Streamlit integration for creating dashboards
- **Jupyter Support**: Full support for Jupyter notebooks
- **Code Quality**: Pre-configured with black, ruff, and mypy
- **Testing**: pytest setup with coverage reporting
- **Documentation**: MkDocs setup with Material theme

### Quick Start

1. Install Poetry (see [Installation Guide](docs/install.md))
2. Clone the repository
3. Install dependencies:

   ```bash
   poetry install
   ```

4. Activate the environment:

   ```bash
   poetry env activate
   ```

---

## Basic Usage

### Working in Notebooks

To enable autoreload in notebooks use the following magic command at the start of your notebook. This will automatically reload any changes to your code.

```python
%load_ext autoreload
%autoreload 2
```

### Data Management

```python
from {{ cookiecutter.module_name }}.utils.paths import data_raw_dir
from {{ cookiecutter.module_name }}.data.data_loader import load_csv

# Process raw data
df = load_csv(data_raw_dir('input.csv'))
```

### Model Development

```python
from {{ cookiecutter.module_name }}.utils.paths import data_processed_dir
from {{ cookiecutter.module_name }}.models import train_model

# Train model
model = train_model(
    data_path=data_processed_dir('train.csv'),
    model_type='random_forest'
)
```

### Visualization

```python
from {{ cookiecutter.module_name }}.utils.paths import reports_figures_dir
from {{ cookiecutter.module_name }}.visualization.visualize import plot_distribution

# Create visualization
plot_distribution(
    data=results_df,
    save_path=reports_figures_dir('results.png'),
)
```

---

## Project Organization

Please refer to the project structure tree in the [project_structure.md](docs/project_structure.md) for a detailed overview of the directory layout and file organization.

---

## Documentation

- [Installation Guide](docs/install.md): Detailed installation instructions
- [User Guide](docs/user_guide.md): How to use the project
- [Developer Guide](docs/developer_guide.md): Development guidelines
- [Project Structure](docs/project_structure.md): Detailed project structure
- [Contributing Guide](docs/contributing.md): How to contribute
- [Code of Conduct](docs/code_of_conduct.md): Community guidelines

---

## License

This project is licensed under the {{ cookiecutter.license }} License - see the [LICENSE](LICENSE) file for details.
