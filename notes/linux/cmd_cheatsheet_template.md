# Cheatsheet for <placeholder\> command

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

The following document provides an overview of some of the details regarding the use of the Linux `<placeholder>` command as well as a cookbook of practical examples demonstrating the use of the command.  
The first portion of the document consists of details and explanations from the `man` pages for `<placeholder>` as well as some summaries of the details regarding the usage of the `<placeholder>` command.  
The second part consists of practical examples of `<placeholder>` usages to solve specific search & action requirements.


### Name

    <placeholder> - print lines that match patterns

### Description
    
>    `<placeholder>` searches for PATTERNS in each FILE. *PATTERNS* is one or more
    patterns separated by newline characters, and `<placeholder>` prints each line that
    matches a pattern. Typically *PATTERNS* should be quoted when `<placeholder>` is used
    in a shell command.  
    A *FILE* of "`-`" stands for standard input. If no *FILE* is given,
    recursive searches examine the working directory, and nonrecursive searched
    read standard input.

---

### Synopsis

The syntax structure for searching with `<placeholder>` looks like this:
    
       <placeholder> [*OPTION*...] *PATTERNS* [*FILE*...]
       <placeholder> [*OPTION*...] -e *PATTERNS* ... [*FILE*...]
       <placeholder> [*OPTION*...] -f *PATTERN_FILE* ... [*FILE*...]    
    
The command has, essentially, two sections which can be briefly summarized as:

    <placeholder> "<pattern>" <input>

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
  

As with all items outlined here, refer to [`man <placeholder>`](https://manned.org/<placeholder>) for additional, specific details.

---

### Regular Expressions

---

### Examples

* [Example command one](#example-command-one)
* [Example command two](#example-command-two)
* [Example command three](#example-command-three)
* [Example command four](#example-command-four)
* [Example command five](#example-command-five)

The following examples make up the `<placeholder>` command cookbook

#### Example command one
 
```
    <placeholder> 'kbowen' /etc/passwd   # search for lines containing 'kbowen' in /etc/passwd
    <placeholder> kbowen /etc/passwd     # quotes usually not needed when not using regex patterns
    <placeholder> import *.py            # search multiple files
```

#### Example command two
 
```
    <placeholder> -i kbowen users.txt    # find kbowen, Kbowen, KBowen, KBOWEN, etc.
```

#### Example command three

```
    <placeholder> -o "upgrade" /var/log/dpkg.log     # Only print pattern not whole line
```

#### Example command four

```
    <placeholder> -c "upgrade" /var/log/dpkg.log     # Output only match count
```

#### Example command five

```
    <placeholder> "upgrade" --exclude="alternatives.log" /var/log/*.log
```

---

### Resources

Most the information & examples provided above were originally sourced from the following resources:

  - [Linux man page - <placeholder>](https://manned.org/<placeholder>)
  - [Alvin Alexander - <placeholder>](https://alvinalexander.com/blog/post/linux-unix/find-files-containing-two-or-more-regular-expressions/)
  - [The Mouseless Dev](https://themouseless.dev/posts/<placeholder>-basics-mouseless/)
