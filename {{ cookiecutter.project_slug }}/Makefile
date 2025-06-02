# Makefile for {{ cookiecutter.project_name }}

# Default Python binary
PYTHON := poetry run python

# Directories to check
SRC_DIRS := src app/main.py tests

# Help command
.PHONY: help
help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-18s\033[0m %s\n", $$1, $$2}'

install: ## Install all dependencies (base + dev + extras)
	poetry install --with dev,notebook,data-science,viz,test

install-dev: ## Install only dev dependencies
	poetry install --with dev

install-notebook: ## Install notebook dependencies
	poetry install --with notebook

install-data: ## Install data-science dependencies and viz dependencies
	poetry install --with data-science,viz

install-test: ## Install testing dependencies
	poetry install --with test

install-minimal: ## Install base (no extras)
	poetry install

run: ## Run the application (example main)
	$(PYTHON) app/main.py

setup: ## Run full environment setup
	bash scripts/setup_env.sh
	
notebook: ## Launch Jupyter Lab
	poetry run jupyter lab

lint: ## Run ruff linter on src and app/main.py
	poetry run ruff check $(SRC_DIRS)

format: ## Format code with black
	poetry run black $(SRC_DIRS)

typecheck: ## Run type checks with mypy
	poetry run mypy $(SRC_DIRS)

test: ## Run pytest on tests
	poetry run pytest --cov=src

test-watch: ## Auto-rerun tests on file change
	poetry run ptw --runner "pytest --cov=src"

clean: ## Remove Python cache and build artifacts
	rm -rf __pycache__ .pytest_cache .mypy_cache dist build *.egg-info
