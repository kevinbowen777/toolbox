#!/bin/env python

"""Create Github issues labeled enhancement for Django repositories."""


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
    # "library",
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
            "enhancement",
            "--title",
            "Add footer",
            "--body",
            "See https://github.com/kevinbowen777/library/blob/master/templates/base.html for details",
            "--assignee",
            "@me",
        ]
    )
    os.chdir("..")
