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
    "djapi-todo",
    "djapi-blog",
]

for x in repo_list:
    # gh label create "deployment" -c "#52794f" -d "project release & publishing"
    # gh label create "testing" -c "#5319e7" -d "project testing & validation"
    # cmd = "gh issue list"
    os.chdir(x)
    subprocess.run(
        [
            "gh",
            "label",
            "create",
            "deployment",
            "-c",
            "#52794f",
            "-d",
            "project release & publishing",
        ]
    )
    os.chdir("..")
