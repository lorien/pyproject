# Default Python Project Template README

This project is created with cookiecutter using template located at https://github.com/lorien/pyproject

To create another project from this template, run the command "cookiecutter gh:lorien/pyproject"

## Initial Project Setup

To create virtual environment and install all dependencies run: `make bootstrap`

You can change dependencies in "requirements.txt" file


## Database

By default the project is configured to use MongoDB. To change MongoDB connection settings update "var/config.yml" file.

## Scripts

Command line scripts are stored in "script/" directory and can be launched with `run`
command which is provided by "runscript" package.

Example. You have "script/foo.py" file. If you run console command "run foo", the runscript
framework will run `main()` function from "script/foo.py" file.


## Support

Telegram English chat: [grablab](https://t.me/grablab)

Telegram Russian chat: [grablab\_ru](https://t.me/grablab_ru)
