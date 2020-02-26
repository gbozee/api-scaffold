#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath, is_directory=False):
    path = os.path.join(PROJECT_DIRECTORY, filepath)
    if is_directory:
        shutil.rmtree(path)
    else:
        os.remove(path)


if __name__ == "__main__":

    if "no" in "{{ cookiecutter.zeit_now_deploy|lower }}":
        cli_file = "now.json"
        remove_file(cli_file)
        cli_file = ".nowignore"
        remove_file(cli_file)
    if "no" in "{{ cookiecutter.sql_database|lower }}":
        cli_file = "migrations"
        remove_file(cli_file, True)
        cli_file = "alembic.ini"
        remove_file(cli_file)

