# Python Project Template for Cookiecutter

This is a [cookiecutter](https://github.com/cookiecutter/cookiecutter) template I use to start a
new python project.

## Template features

- Makefile for "make" utility to run linters, tests and other things
- Tools to build virtual environment and install project requirements
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

## Usage

* Install cookiecutter: `pip install cookiecutter`
* Run command: `cookiecutter gh:lorien/pyproject` and provide answers
    for questions which cookiecutter will ask you. The value of "project\_name" will be
    used to create a new directory with project contents.


## Feedback

Telegram English chat: [https://t.me/grablab](https://t.me/grablab)

Telegram Russian chat: [https://t.me/grablab\_ru](https://t.me/grablab_ru)
