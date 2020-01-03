#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == "__main__":


    if "no" in "{{ cookiecutter.auth_backend|lower }}":
        cli_file = os.path.join("{{ cookiecutter.project_slug }}", "auth_backends.py")
        remove_file(cli_file)

