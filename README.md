# Python Project Template for Cookiecutter

This is a template for [cookiecutter](https://github.com/cookiecutter/cookiecutter) to create
starting set of files for a new python project.

Features:

- Makefile with "make" commands to run linters, tests and other utilities
- Default configurations for all tools used in the template
- Linters:
    - flake8 and a number of flake8 plugins
    - pylint
    - bandit
- Type checkers:
    - mypy
- Tests:
    - pytest
- Most of tool's configs are stored in pyproject.toml
- Tools to build python package and upload it to pypi

Usage:

* Install cookiecutter: `pip install cookiecutter`
* Run command: `cookiecutter gh:lorien/pyproject` and provide answers
    for questions which cookiecutter will ask you. The value of "project\_name" will be
    used to create a new directory with project contents.


## Community

Telegram English chat: [https://t.me/grablab](https://t.me/grablab)

Telegram Russian chat: [https://t.me/grablab\_ru](https://t.me/grablab_ru)
