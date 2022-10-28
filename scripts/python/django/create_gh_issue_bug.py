#!/bin/env python

"""Create Github issues labeled bug for Django repositories."""

import os
import subprocess


repo_list = [
    "bookstore",
    # "cheese",
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
    "api/djapi-library",
    "djapi-todo",
    "djapi-blog",
]

for repo in repo_list:
    os.chdir(repo)
    subprocess.run(
        [
            "gh",
            "issue",
            "create",
            "--label",
            "bug",
            "--title",
            "This is a bug",
            "--body",
            "",
            "--assignee",
            "@me",
        ]
    )
    os.chdir("..")
