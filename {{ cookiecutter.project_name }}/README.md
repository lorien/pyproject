## What is this

This is default README from template I use to start almost any python project. You can get this template from https://github.com/lorien/spider\_project.


## Installation

To create virtual environment and install all dependencies run: `make build`

You can change dependencies in "requirements.txt" file


## Database

By default the project is configured to use MongoDB. To change MongoDB connection settings and database name change `MONGODB\_CONNECTION` and `MONGODB\_NAME` in the "project/settings\_local.py" file which is imported by
"project/settings.py" file. File "project/settings\_local.py" must be excluded
from repository using ignore file. DO NOT change "roject/settings.py"
file.


## Scripts

Command line custom scripts are stored in "script/" directory and launched with `run`
command which is provided by "runscript" package. So, if there is "script/foo.py"
file the command `run foo` will run `main()` function from "script/foo.py" file.


## Support

Telegram chats: [grablab](https://t.me/grablab) (English) and [grablab\_ru](https://t.me/grablab_ru) (Russian)
