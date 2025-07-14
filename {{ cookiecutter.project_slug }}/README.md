# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Project Overview

This project is a data science template that provides a solid foundation for building data-driven applications using Python. It includes:

- **Modern Python Development**: Using Poetry for dependency management
- **Data Science Tools**: Integration with popular data science libraries
- **Development Tools**: Code quality tools and testing frameworks
- **Project Structure**: Organized directory structure for data science projects
- **Documentation**: Comprehensive documentation using MkDocs

## Key Features

- **Dependency Management**: Using Poetry for reliable dependency management
- **Data Version Control**: Optional DVC integration for data versioning
- **ML Experiment Tracking**: Optional MLflow integration for experiment tracking
- **Interactive Dashboards**: Optional Streamlit integration for creating dashboards
- **Jupyter Support**: Full support for Jupyter notebooks
- **Code Quality**: Pre-configured with black, ruff, and mypy
- **Testing**: pytest setup with coverage reporting
- **Documentation**: MkDocs setup with Material theme

## Installation Steps

Please read [install.md](docs/install.md) for details on how to set up this project.

### Quick Start

1. Install Poetry (see [Installation Guide](docs/install.md))
2. Clone the repository
3. Install dependencies:
   ```bash
   poetry install
   ```
4. Activate the environment:
   ```bash
   poetry shell
   ```

## Basic Usage

### Data Management

```python
from {{ cookiecutter.module_name }}.data import process_data

# Process raw data
df = process_data('data/raw/input.csv')
```

### Model Development

```python
from {{ cookiecutter.module_name }}.models import train_model

# Train model
model = train_model(
    data_path='data/processed/train.csv',
    model_type='random_forest'
)
```

### Visualization

```python
from {{ cookiecutter.module_name }}.visualization import plot_results

# Create visualization
plot_results(
    data=results_df,
    output_path='reports/figures/results.png'
)
```

### Interactive Dashboard

```bash
poetry run streamlit run src/{{ cookiecutter.module_name }}/visualization/dashboard.py
```

## Example Outputs

The project includes example outputs in the following locations:

- **Reports**: Generated reports in `reports/`
- **Figures**: Visualizations in `reports/figures/`
- **Notebooks**: Example notebooks in `notebooks/`

## Project Organization

Please refer to the project structure tree in the [project_structure.md](docs/project_structure.md)

```
{{ cookiecutter.project_slug }}/
├── data/               # Data files
│   ├── raw/           # Raw data
│   └── processed/     # Processed data
├── docs/              # Documentation
├── notebooks/         # Jupyter notebooks
├── reports/           # Generated reports
├── src/               # Source code
│   └── {{ cookiecutter.module_name }}/
│       ├── data/      # Data loading utilities
│       ├── features/  # Feature engineering
│       ├── models/    # Model training and evaluation
│       └── viz/       # Visualization utilities
├── tests/             # Test files
├── pyproject.toml     # Project configuration
└── README.md          # Project overview
```

## Available Tools

### Data Science Tools
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Scikit-learn**: Machine learning
- **MLflow**: Experiment tracking
- **DVC**: Data version control
- **Streamlit**: Interactive dashboards

### Development Tools
- **Poetry**: Dependency management
- **Black**: Code formatting
- **Ruff**: Fast Python linter
- **MyPy**: Static type checking
- **Pre-commit**: Git hooks
- **Pytest**: Testing framework

### Visualization Tools
- **Matplotlib**: Basic plotting
- **Seaborn**: Statistical visualization
- **Plotly**: Interactive plots
- **Bokeh**: Interactive visualization

## Documentation

- [Installation Guide](docs/install.md): Detailed installation instructions
- [User Guide](docs/user_guide.md): How to use the project
- [Developer Guide](docs/developer_guide.md): Development guidelines
- [Project Structure](docs/project_structure.md): Detailed project structure
- [Contributing Guide](docs/contributing.md): How to contribute
- [Code of Conduct](docs/code_of_conduct.md): Community guidelines

## Contribution Guidelines

Please read our [Contributing Guide](docs/contributing.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the {{ cookiecutter.license }} License - see the [LICENSE](LICENSE) file for details.