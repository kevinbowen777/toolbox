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
    # "django_start",
    "learning_log",
    "library",
    "message_board",
    "news",
    "pastebin-drf-api",
    "superlists",
    "api/djapi-library",
    "djapi-todo",
    "djapi-blog",
]

for repo in repo_list:
    os.chdir(repo)
    print(f"Starting cleanup of {repo} nox files...")
    subprocess.run(
        [
            "rm",
            "-rf",
            ".nox/black-3-9/",
            ".nox/black-3-10/",
            ".nox/black-3-11/",
            ".nox/docs-3-9/",
            ".nox/docs-3-10/",
            ".nox/docs-3-11/",
            ".nox/lint-3-9/",
            ".nox/lint-3-10/",
            ".nox/lint-3-11/",
            ".nox/safety-3-9/",
            ".nox/safety-3-10/",
            ".nox/safety-3-11/",
            ".nox/tests-3-9/",
            # ".nox/tests-3-10/",
            ".nox/tests-3-11/",
        ]
    )
    print(f"Finished cleanup of {repo} nox files.")
    os.chdir("..")
