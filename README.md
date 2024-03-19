# Python Project Template for Cookiecutter

This is a [cookiecutter](https://github.com/cookiecutter/cookiecutter) template I use to start
new python project.

Features of this template:

- Makefile with "make" commands to run linters, tests and other utilities
- Default configurations for all tools used in the template
- Linters:
    - ruff with almost all rules enabled
    - pylint
- Type checkers:
    - mypy in strict mode
- Tests:
    - pytest
- Tool's configurations are stored in pyproject.toml
- Tools to build python package and upload it to pypi

Usage:

* Install cookiecutter: `pip install cookiecutter`
* Run command: `cookiecutter gh:lorien/pyproject` and provide answers
    for questions which cookiecutter will ask you. The value of "project\_name" will be
    used to create a new directory with project contents.


## Community

Telegram English chat: [https://t.me/grablab](https://t.me/grablab)

Telegram Russian chat: [https://t.me/grablab\_ru](https://t.me/grablab_ru)
