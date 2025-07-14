# {{ cookiecutter.project_name }}

Welcome to the **{{ cookiecutter.project_name }}** documentation! This project is a data science template that provides a solid foundation for building data-driven applications using Python.

## Overview

This project template is designed to help you quickly set up and start working on data science projects with best practices in mind. It includes:

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

## Quick Start

1. Install Poetry (see [Installation Guide](install.md))
2. Clone the repository
3. Install dependencies:
   ```bash
   poetry install
   ```
4. Activate the environment:
   ```bash
   poetry shell
   ```

## Project Structure

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

- [Installation Guide](install.md): Detailed installation instructions
- [User Guide](user_guide.md): How to use the project
- [Developer Guide](developer_guide.md): Development guidelines
- [API Reference](api.md): API documentation
- [Project Structure](project_structure.md): Detailed project structure

## Contributing

Please read our [Contributing Guide](contributing.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the {{ cookiecutter.license }} License - see the [LICENSE](../LICENSE) file for details.
