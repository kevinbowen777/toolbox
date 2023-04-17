# Cheatsheet for grep command

Looking for a specific command?  
Jump to the [Examples](#examples) section.


  * [Introduction](#introduction)
  * [Name](#name)
  * [Description](#description)
  * [Synopsis](#synopsis)
  * [Options](#options)
  * [Regular Expressions](#regular-expressions)
  * [Examples](#examples)
  * [Resources](#resources)

---

### Introduction

The following document provides an overview of some of the details regarding the use of the Linux `grep` command as well as a cookbook of practical examples demonstrating the use of the command.  
The first portion of the document consists of details and explanations from the `man` pages for `grep` as well as some summaries of the details regarding the usage of the `grep` command.  
The second part consists of practical examples of `grep` usages to solve specific search & action requirements.


### Name

    grep - print lines that match patterns

### Description
    
    `grep` searches for PATTERNS in each FILE. *PATTERNS* is one or more
    patterns separated by newline characters, and `grep` prints each line that
    matches a pattern. Typically *PATTERNS* should be quoted when `grep` is used
    in a shell command.  
    A *FILE* of "`-`" stands for standard input. If no *FILE* is given,
    recursive searches examine the working directory, and nonrecursive searched
    read standard input.

---

### Synopsis

The syntax structure for searching with `grep` looks like this:
    
       grep [*OPTION*...] *PATTERNS* [*FILE*...]
       grep [*OPTION*...] -e *PATTERNS* ... [*FILE*...]
       grep [*OPTION*...] -f *PATTERN_FILE* ... [*FILE*...]    
    
The command has, essentially, two sections which can be briefly summarized as:

    grep "<pattern>" <input>

The `"<pattern>"` is a regular expression and the `<input>` can be what you
enter in your terminal or a file.    

---

### Options
  - Pattern Syntax
  - Matching Control
  - General Output Control
  - Output Line Prefix Control
  - Context Line Control
  - File and Directory Selection
  - Other Options
  

As with all items outlined here, refer to [`man grep`](https://manned.org/grep) for additional, specific details.

---

### Regular Expressions

---

### Examples

    * [search for a string in one or more files](#search-for-a-string-in-one-or-more-files)
    * [case-insensitive](#case-insensitive)
    * [regular expressions](#regular-expressions)
    * [display matching filenames, not lines](#display-matching-filenames,-not-lines)
    * [show matching line numbers](#show-matching-line-numbers)
    * [lines before and after grep match](#lines-before-and-after-grep-match)
    * [reverse the meaning](#reverse-the-meaning)
    * [grep in a pipeline](#grep-in-a-pipeline)
    * [search for multiple patterns](#search-for-multiple-patterns)
    * [multiple search strings, multiple filename patterns](#multiple-search-strings,-multiple-filename-patterns)
    * [grep + find](#grep-+-find)
    * [recursive grep search](#recursive-grep-search)
    * [grep gzip files](#grep-gzip-files)

The following examples make up the `grep` command cookbook

#### search for a string in one or more files
 
```
    grep 'kbowen' /etc/passwd   # search for lines containing 'kbowen' in /etc/passwd
    grep kbowen /etc/passwd     # quotes usually not needed when not using regex patterns
    grep import *.py            # search multiple files
```

#### case-insensitive
 
```
    grep -i kbowen users.txt    # find kbowen, Kbowen, KBowen, KBOWEN, etc.
```

#### regular expressions
 
```
    grep '^kbowen' /etc/passwd   # find 'kbowen', but only at the start of a line
    grep '[FG]oo' *              # find Foo or Goo in all files in the current dir
    grep '[0-9][0-9][0-9]' *     # find all lines in all files in the current dir with three numbers in a row
```

#### display matching filenames, not lines
 
```
    grep -l import *.py    # show all filenames containing the string 'import'
    grep -il import *.py   # same thing, case-insensitive
```

#### show matching line numbers
 
    grep -n we gettysburg-address.txt    # show line numbers as well as the matching lines

#### lines before and after grep match
 
```
    grep -B5 "the living" gettysburg-address.txt        # show all matches, and five lines before each match
    grep -A10 "the living" gettysburg-address.txt       # show all matches, and ten lines after each match
    grep -B5 -A5 "the living" gettysburg-address.txt    # five lines before and ten lines after
```

#### reverse the meaning
 
```
    grep -v kbowen /etc/passwd      # find any line *not* containing 'kbowen'
    grep -vi kbowen /etc/passwd     # same thing, case-insensitive
```

#### grep in a pipeline
 
```
    ps auxwww | grep urxvt          # all processes containing 'urxvt'
    ps auxwww | grep -i build        # all processes containing 'build', ignoring case
    ls -al | grep '^d'              # list all dirs in the current dir
```

#### search for multiple patterns
 
```
    egrep -d skip 'exclude|registration' *  # search for multiple patterns, all files in current dir
    egrep -id skip 'exclude|registration' *  # same thing, case-insensitive
    egrep 'score|nation|liberty|equal' gettysburg-address.txt  # all lines matching multiple patterns
    locate -i calendar | grep Users | egrep -vi 'twiki|gif|shtml|drupal-7|java|PNG' 
```

See also:   http://alvinalexander.com/linux-unix/linux-egrep-multiple-regular-expressions-regex

#### multiple search strings, multiple filename patterns
 
```
    grep -li "4.2.x" $(find . -name "*.md" -exec grep -li "regitstration" {} \;) 
    # find all files named "*.java,v" containing both '4.2.x' and 'registration'
```                                            

#### grep + find
 
```
    find . -type f -exec grep -il 'kevin.bowen' {} \;
    # print all filenames of files under current dir containing 'foo', case-insensitive
```

#### recursive grep search
 
```
    grep -rl 'null' .  # similar to the previous find command; does a recursive search
    grep -ril 'null' /home/kbowen/dev /var/www      # search multiple dirs
    egrep -ril 'kevin|kbowen' .                      # multiple patterns, recursive
```
See also:  http://alvinalexander.com/linux-unix/recursive-grep-r-searching-egrep-find 

#### grep gzip files
 
```
    zgrep foo myfile.gz                      # all lines containing the pattern 'foo'
    zgrep 'GET /blog' access_log.gz          # all lines containing 'GET /blog'
    zgrep 'GET /blog' access_log.gz | more  
```

---

### Resources

Most the information & examples provided above were originally sourced from the following resources:

  - [Linux man page - grep](https://manned.org/grep)
  - [Alvin Alexander - grep](https://alvinalexander.com/blog/post/linux-unix/find-files-containing-two-or-more-regular-expressions/)
  - [The Mouseless Dev](https://themouseless.dev/posts/grep-basics-mouseless/)
