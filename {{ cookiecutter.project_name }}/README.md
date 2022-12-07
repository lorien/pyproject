# Default Python Project Template README

This project is created with cookiecutter using template located at https://github.com/lorien/pyproject

To create another project from this template, run the command "cookiecutter gh:lorien/pyproject"


## Initial Project Setup

To create virtual environment and install all dependencies run: `make bootstrap`

You can change dependencies in "requirements.txt" file


# Type checking and linters

Run command "make check" to run mypy, pylint, flake8 and bandit linters on your files. Do not forget
to update FILES\_CHECK\_MYPY and FILES\_CHECK\_ALL in Makefile to include all packages and modules
you want to check.


## Database

By default the project is configured to use MongoDB. To change MongoDB connection settings update "var/config.yml" file.


## Scripts

Command line scripts are stored in "script/" directory and can be launched with `run`
command which is provided by "runscript" package.

Example. You have "script/foo.py" file. If you run console command "run foo", the runscript
framework will run `main()` function from "script/foo.py" file.


## Community

Telegram English chat: [https://t.me/grablab](https://t.me/grablab)

Telegram Russian chat: [https://t.me/grablab\_ru](https://t.me/grablab_ru)
