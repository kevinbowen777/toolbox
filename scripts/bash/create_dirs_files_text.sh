#!/bin/bash

#{{{ ======================================================================= #
# Author: Kevin Bowen <kevin.bowen@gmail.com>
# Script Name: create_dirs_files_text.sh
# Description:
#		  Create dirs & subdirs with multiple files and add text to files
#
#    This script will create the following directory tree
#
#                .testdir
#                ├── topdir1
#                │   ├── dir_a
#                │   │   ├── file1.txt
#                │   │   ├── file2.txt
#                │   │   └── file3.txt
#                │   ├── dir_b
#                │   │   ├── file1.txt
#                │   │   ├── file2.txt
#                │   │   └── file3.txt
#                │   └── dir_c
#                │       ├── file1.txt
#                │       ├── file2.txt
#                │       └── file3.txt
#                └── topdir2
#                    ├── dir_a
#                    │   ├── file1.txt
#                    │   ├── file2.txt
#                    │   └── file3.txt
#                    ├── dir_b
#                    │   ├── file1.txt
#                    │   ├── file2.txt
#                    │   └── file3.txt
#                    └── dir_c
#                        ├── file1.txt
#                        ├── file2.txt
#                        └── file3.txt
#
# Source : http://www.github.com/kevinbowen777/toolbox.git
# Last modified: 20230315
# Dependencies:
#	bash >= 4.0.0
#     
#}}} ======================================================================= #

shopt -s globstar

mkdir testdir && cd "$_" || exit

# Specify number of top-level directories
for d in {1..2}
do
    # Specify number of sub-directories
    mkdir -p topdir"${d}"/dir_{a..c}
    # Specify number of files in each subdirectory
    touch topdir"${d}"/dir_{a..c}/file{1..3}.txt
    for filename in ./**/*.txt
    do
        echo hello > "${filename}"
    done
done
