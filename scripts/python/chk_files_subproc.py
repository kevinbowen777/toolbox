#!/usr/bin/env python3

"""
Name: chk_files.py
Purpose:
    Check existance of sqlite3 files from selected
        projects using subprocess module.
           https://github.com/kevinbowen777/

source: https://github.com/kevinbowen777/toolbox
version: 0.2.0
created: 20220922
updated: 20221027
@author: kevin.bowen@gmail.com

References on using subprocess.run()
https://stackoverflow.com/a/51950538/1704582
"""

import argparse
import os
import subprocess
import sys


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
    print(
        "No framework was specified.\nDefault to running on" " all of the projects...."
    )
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
    os.chdir(project)
    for repo in repos[project]:
        print(f"    Checking in {repo} repo:")
        os.chdir(repo)
        p = subprocess.Popen(
            "ls *.sqlite3",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            # check=True,
            text=True,
        )
        result, err = p.communicate()
        if result == "":
            print("\tNo file found")
        else:
            print(f"\t{result.strip()}")
        os.chdir("..")
    os.chdir("..")


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
