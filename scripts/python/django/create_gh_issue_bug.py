#!/usr/bin/env python3

"""
Name: create_gh_issue_bug.py
Purpose: Takes a dictionary of parent directories(keys) and
    subdirectories(values), iterates over them and executes
    supplied commands.
    Create GitHub issues with the label 'bug' using the gh CLI tool.
           https://github.com/kevinbowen777/

source: https://github.com/kevinbowen777/utils
version: 0.2.0
created: 20220922
updated: 20221027
@author: kevin.bowen@gmail.com
"""

import argparse
import os
import subprocess
import sys
import time

parser = argparse.ArgumentParser(
    description="run commands in groups of projects"
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
    help="specify a web framework group to run" " commands on",
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
        # "bookstore",
        "cheese",
        "django-todo",
        "django-blog",
        "django-polls",
        # "django-start",
        "learning-log",
        "library",
        "message-board",
        "news",
        # "superlists",
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
    time.sleep(1)
    for repo in repos[project]:
        os.chdir(repo)
        print(f"\n    Creating GitHub bug issue for the {repo} repository:")
        # print(f"\t{repo}...", end='')
        # Add commands to run below.
        subprocess.run(
            [
                "gh",
                "issue",
                "create",
                "--label",
                "bug",
                "--title",
                "Nox tests-3.9 failing",
                "--body",
                "All nox tests are passing with the exception of tests-3.9. Check dev testing packages.",
                "--assignee",
                "@me",
            ]
        )
        # If commands will take longer than an instant, you may
        # consider indicating when they are complete.
        # print("done!")
        os.chdir("..")


def select_parent(framework):
    """Select the parent to directory to enter."""
    if framework == "all":
        confirm = query_yes_no(f"Are you sure?")

        if confirm == "yes":
            time.sleep(1)
            for framework in repos:
                walk_and_run(framework)
                os.chdir("..")
        else:
            print("Have a nice day!")
    else:
        print(f"Creating GitHub bug issues for the {framework} projects.")
        time.sleep(1)
        walk_and_run(framework)


if __name__ == "__main__":
    try:
        framework = args.framework
        select_parent(framework)
    except KeyboardInterrupt:
        print()
        print(f"Stopped {os.path.basename(__file__)}. Exiting...")
        sys.exit()
