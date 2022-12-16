import os
import sys


def main():
    if "{{ cookiecutter.packaging }}" != "yes":
        os.unlink(".bumpversion.cfg")


if __name__ == "__main__":
    main()
