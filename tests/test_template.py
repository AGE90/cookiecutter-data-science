"""
Render the template without the network-dependent hooks and check the output.

Run with: uvx --with cookiecutter pytest tests/
"""

import tomllib
from pathlib import Path

import pytest
from cookiecutter.main import cookiecutter

TEMPLATE_DIR = Path(__file__).resolve().parents[1]
OFFLINE = {"initialize_env": "no", "initialize_git_repository": "no"}


def render(tmp_path, **context):
    """Generate a project into tmp_path and return its path."""
    out = cookiecutter(
        str(TEMPLATE_DIR),
        no_input=True,
        output_dir=str(tmp_path),
        extra_context={**OFFLINE, "project_name": "Demo Proj", **context},
    )
    return Path(out)


@pytest.mark.parametrize("license_", ["MIT", "BSD-3-Clause", "No license file"])
def test_render(tmp_path, license_):
    project = render(tmp_path, license=license_, python_version="3.13")

    assert project.name == "demo-proj"
    for rel in ["pyproject.toml", "Makefile", "CLAUDE.md", "src/demo_proj/__init__.py"]:
        assert (project / rel).is_file(), rel
    assert (project / "LICENSE").exists() == (license_ != "No license file")

    pyproject = tomllib.loads((project / "pyproject.toml").read_text())
    assert pyproject["project"]["name"] == "demo_proj"
    assert pyproject["project"]["requires-python"] == ">=3.13"
    assert pyproject["project"].get("license") == (
        None if license_ == "No license file" else license_
    )
    assert pyproject["tool"]["ruff"]["target-version"] == "py313"

    leftovers = [
        p for p in project.rglob("*")
        if p.is_file() and "{{" in p.read_text(errors="ignore")
    ]
    assert not leftovers, leftovers


@pytest.mark.parametrize("enabled", ["yes", "no"])
def test_optional_tools_are_left_out(tmp_path, enabled):
    project = render(tmp_path, use_mlflow=enabled, use_dvc=enabled)
    generated = "\n".join(
        p.read_text()
        for p in [project / "Makefile", project / "README.md", *project.rglob("*.py")]
    )

    assert ("mlflow" in generated) == (enabled == "yes")
    assert ("dvc" in generated) == (enabled == "yes")


def test_invalid_input_fails(tmp_path):
    with pytest.raises(Exception):
        render(tmp_path, author_email="not-an-email")
