#!/usr/bin/env python3

"""
Name: chk_files.py
Purpose:
    Check existance of sqlite3 files from selected
        projects using pathlib module.
           https://github.com/kevinbowen777/

source: https://github.com/kevinbowen777/toolbox
version: 0.2.0
created: 20220922
updated: 20221027
@author: kevin.bowen@gmail.com
"""

import argparse
import sys

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


parser = argparse.ArgumentParser(
    description="Check existance of files "
    "based on a directory structure ordered by framework."
)
parser.add_argument(
    "-f",
    "--framework",
    action="store",
    choices=[
        "django",
        "drf",
        "flask",
        "fastapi",
        "all",
    ],
    help="specify a group to run command on",
)
parser.add_argument("--version", action="version", version="%(prog)s 0.2.0")
args = parser.parse_args()
if args.framework is None:
    print("No group was specified.\nDefault to running on" " all of the projects....")
    args.framework = "all"


repos = {
    "django": [
        "bookstore",
        "cheese",
        "django-todo",
        "django-blog",
        "django-polls",
        "django-start",
        "learning-log",
        "library",
        "message-board",
        "news",
        "superlists",
    ],
    "drf": [
        "django-api-blog",
        "django-api-library",
        # "django-api-todo", DO NOT RUN - dir structure not compatible with script
        "djapi-blog",
        "djapi-library",
        "djapi-todo",
        "pastebin-drf-api",
    ],
    "flask": [
        "flaskblog",
        "flask-chat",
    ],
    "fastapi": [
        "recipes",
    ],
}


def query_yes_no(question, answer="no"):
    """Handles confirmation prompts."""
    valid = {"yes": "yes", "y": "yes", "no": "no", "n": "no"}
    prompt = " [(Y)es/(N)o] "

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        try:
            if answer is not None and choice == "":
                return answer
            elif answer in valid:
                return valid[choice]
        except KeyError:
            sys.stdout.write("Please respond with 'yes' or 'no' " "(or 'y' or 'n').\n")


def walk_and_run(project):
    """Enter the framework's subdirectories and run the commands
    specified below.
    """
    for repo in repos[project]:
        p = Path(BASE_DIR / project / repo)
        suffix = ".sqlite3"
        count = 0
        print(f"    Checking in {repo} repo:")
        for file in p.iterdir():
            if file.match("*.sqlite3"):
                print(f"\t{file.name}")
                count += 1
            else:
                continue
        if count == 0:
            print("\tNo file found.")


def select_parent(framework):
    """Select the parent to directory to enter."""
    if framework == "all":
        confirm = query_yes_no(f"Are you sure?")

        if confirm == "yes":
            for framework in repos:
                print(f"Checking files from the {framework} projects.")
                walk_and_run(framework)
        else:
            print("Have a nice day!")
    else:
        print(f"Checking files from the {framework} projects.")
        walk_and_run(framework)


if __name__ == "__main__":
    try:
        framework = args.framework
        select_parent(framework)
    except KeyboardInterrupt:
        print()
        print(f"Stopped {Path(__file__).name}. Exiting....")
        sys.exit()
