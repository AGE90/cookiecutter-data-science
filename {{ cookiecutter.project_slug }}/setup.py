import pathlib
from setuptools import setup, find_packages

def readme() -> str:
    """Utility function to read the README.md.
    Used for the `long_description`.

    Returns:
        The content of the README.md file as a string.
    """
    readme_path = pathlib.Path(__file__).parent / 'README.md'
    with readme_path.open(encoding='utf-8') as f:
        return f.read()

setup(
    name='{{ cookiecutter.module_name }}',
    version='{{ cookiecutter.project_version }}',
    author='{{ cookiecutter.author_name.replace("\'", "\\\'") }}',
    author_email='{{ cookiecutter.author_email }}',
    description='{{ cookiecutter.project_description }}',
    python_requires='>=3',
    license="{% if cookiecutter.license == 'MIT' %}MIT{% elif cookiecutter.license == 'BSD-3-Clause' %}BSD-3{% endif %}",
    url='{{ cookiecutter.project_url }}',
    packages=find_packages(),
    long_description=readme(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        # List your package dependencies here
    ],
    extras_require={
        'dev': [
            # List your development dependencies here
        ],
    },
    entry_points={
        'console_scripts': [
            # Define entry points for CLI scripts here
        ],
    },
)
