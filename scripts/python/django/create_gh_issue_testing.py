#!/bin/env python

"""Create Github issues labeled testing for Django repositories."""


import os
import subprocess


repo_list = [
    "bookstore",
    "cheese",
    "djangdo",
    "django_api",
    "django_api-library",
    "django_api-todo",
    "django_blog",
    "django_polls",
    "django_start",
    "learning_log",
    "library",
    "message_board",
    "news",
    "pastebin-drf-api",
    # "superlists",
    "api/djapi-blog",
    "djapi-library",
    "djapi-todo",
]

for repo in repo_list:
    os.chdir(repo)
    subprocess.run(
        [
            "gh",
            "issue",
            "create",
            "--label",
            "testing",
            "--title",
            "Remove isort from pyproject.toml",
            "--body",
            "",
            "--assignee",
            "@me",
        ]
    )
    os.chdir("..")
