import os
import sys


def main():
    if "{{ cookiecutter.packaging }}" != "yes":
        os.unlink(".bumpversion.cfg")
        os.unlink("LICENSE")


if __name__ == "__main__":
    main()
