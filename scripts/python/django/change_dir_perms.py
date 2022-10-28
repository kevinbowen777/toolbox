#!/bin/env python

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
    "superlists",
    "api/djapi-library",
    "api/djapi-todo",
    "api/djapi-blog",
]

for x in repo_list:
    # cmd = "gh issue list"
    os.chdir(x)
    subprocess.run(
        [
            "sudo",
            "chown",
            "-R",
            "kbowen:kbowen",
            "htmlcov",
            ".pytest_cache",
        ]
    )
    os.chdir("..")
