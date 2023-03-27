# Cheatsheet for find command

Looking for a specific command?  
Jump to the [Examples](#examples) section.

  * [Introduction](#introduction)
  * [Name](#name)
  * [Description](#description)
  * [Synopsis](#synopsis)
  * [Options](#options)
  * [Expression](#expression)
      * [Example directory structure](#example-directory-structure)
    * [Test Expressions](#test-expressions)
      * [Filtering empty file](#filtering-empty-file)
      * [Filtering by file name](#filtering-by-file-name)
      * [Filtering by file path](#filtering-by-file-path)
      * [Filtering using a regex](#filtering-using-a-regex)
      * [Case insensitive search](#case-insensitive-search)
      * [Filtering by type of file](#filtering-by-type-of-file)
      * [Filtering by permissions](#filtering-by-permissions)
      * [Filtering by owner or group](#filtering-by-owner-or-group)
    * [Action Expressions](#action-expressions)
      * [Deleting files](#deleting-files)
      * [Running a command on each result](#running-a-command-on-each-result)
      * [Running a command in working directory](#running-a-command-in-working-directory)
      * [Running a command in starting directory](#running-a-command-in-starting-directory)
      * [Changing the output](#changing-the-output)
      * [Writing the output to a file](#writing-the-output-to-a-file)
    * [Operators](#operators)
  * [Examples](#examples)
  * [Resources](#resources)

---

### Introduction

The following document provides an overview of some of the details regarding the use of the Linux `find` command as well as a cookbook of practical examples demonstrating the use of the command.  
The first portion of the document consists of details and explanations from the `man` pages for find as well as some summaries of the details regarding the usage of the `find` command.  
The second part consists of practical examples of `find` usages to solve specific search & action requirements.


### Name

    find - search for files in a directory hierarchy

### Description
    
The `find` command is used to locate files. `find` will search any set of directories you specify for files that match the supplied search criteria. `find` searches the directory tree rooted at each given starting-point by evaluating the given expression.

`find` can search for files, or directories, by:

  - name
  - owner
  - group
  - type
  - permissions
  - date
    
`find` can also be used to execute commands (e.g. `grep`, `mv`, `rm`, etc.) to act upon the query results.

---

### Synopsis

The syntax structure for searching with `find` looks like this:
    
    find [-H] [-L] [-P] [-D debugopts] [-Olevel] [starting-point...] [expression]
    
The command has, essentially, three sections which can be briefly summarized as:

    find <options> <starting-point> <expression>
   
  - *[options\]* - The  `-H`,  `-L`  and `-P` options control the treatment of symbolic links. The `-D` and `-O` options control diagnostic output and query optimisations, respectively.
  - *[starting-point\]* - List of directories where to search
  - *[expression\]* - Expressions filter the search or perform actions on the
  files found.

All arguments to `find` are optional, below are the defaults for each query
section:

  - *[options\]* - defaults to `.` (the current working directory)
  - *[starting-point\]* - defaults to `none` (select all files)
  - *[expressions\]* (known as the ***find action***) - defaults to `‑print` (display the names of found files to standard output).

Technically, the *options* and *actions* are all known as ***find primaries***.

---

### Options

>   The  `-H`,  `-L`  and `-P` options control the treatment of symbolic links. Command-line arguments following these are taken to be names of files or directories to be examined, up to the first argument that begins with `-`, or the argument `(` or `!`. That argument and any following arguments are taken to be the expression describing what is to be searched for. If no paths are given, the current directory is used. If no expression is given, the expression `-print` is used.

  `-P` Never follow symbolic links.
  
  `-L` Follow symbolic links.
  
  `-H` Do not follow symbolic links, except while processing command line
  arguments.
  
  `-D debugopts` Print diagnostic information. For a complete list of valid
  debug options, see the output of `find -D help`.

    - exec       Show diagnostic information relating to -exec, -execdir, -ok and -okdir
    - opt        Show diagnostic information relating to optimisation
    - rates      Indicate how often each predicate succeeded
    - search     Navigate the directory tree verbosely
    - stat       Trace calls to stat(2) and lstat(2)
    - time       Show diagnostic information relating to time-of-day and timestamp comparisons
    - tree       Display the expression tree
    - all        Set all of the debug flags (but help)
    - help       Explain the various -D options  
  
  `Olevel` Enables query optimisation. The `find` program reorders tests to
  speed up execution while preserving the overall effect.
  
  
For example:

    find -O3 -name example.txt -type f -execdir mv {} test.txt \;
  
See [Find Debug Notes](find_cmd_debug_session_notes.md) for examples.

As with all items outlined here, refer to [`man find`](https://manned.org/find) for additional, specific details.

---

### Expression

The part of the command line after the list of starting points is the *expression*. This is  a kind of query specification describing how we match files and what we do with the files that were matched. An expression is composed of a sequence of things:

  - Test expressions
    - Tests return a true or false value, usually on the basis of some property of a file  we are considering. The `-empty` test for example is true only when the current file is empty.
  - Action expressions
    - Actions have side effects (such as printing something on the standard output)  and return either true or false, usually based on whether or not they are successful. The `-print` action for example prints the name of the current file on the standard output.
  - Global options
    - Global options affect the operation of tests and actions specified on any part of the command line. Global options always return true. The `-depth` option for example makes `find` traverse the file system in a depth-first order.
  - Positional options
    - Positional options affect only tests or actions which follow them. Positional options always return true. The `-regextype` option for example is positional, specifying the  regular expression dialect for regular expressions occurring later on the command line.
  - Operators
    - Operators join together the other items within the expression. They include for example `-o` (meaning logical **OR**) and `-a` (meaning logical **AND**). Where an operator is missing, -a is assumed.

When using multiple expressions without specifying any operator, the **AND** operator is implicitly used.

##### Example Directory Structure

Many of the examples that follow will be using the directory structure below:

```
            .testdir        # (root/current working directory)
            ├── example.txt
            ├── image.jpg
            ├── topdir1
            │   ├── dir_a
            │   │   └── image.jpg
            │   ├── dir_b
            │   │   ├── example.txt
            │   │   └── image.jpg
            │   ├── dir_c
            │   └── image.jpg
            ├── topdir2
            │   ├── dir_a
            │   │   └── image.jpg
            │   ├── dir_b
            │   ├── dir_c
            │   │   └── image.jpg
            │   ├── myfile.txt
            │   └── myfile1.txt
            └── topdir3
                ├── dir_a
                │   └── image.jpg
                ├── dir_b
                │   └── MyFile.txt
                └── image.jpg
                
# Note: for the purposes of the examples in this document, the `folder.jpg` & `myfile1.txt` should *not* be empty files. Use an actual file containing an image/text of any size. 
```

Here is a basic example that decomposes a simple `find` command construct and
its respective elements:

    find topdir2 -name "myfile.txt" -perm 644
    
  - `topdir2` - the starting point of the search.
  - `-name` - A test expression.
  - `"myfile.txt"` - Value of the expression `-name`.
  - `-perm` - Another test expression.
  - `644` - The value of the expression `-perm`.

#### Test Expressions

Test expressions are used to filter the folders and files.

##### Filtering Empty File

The `-empty` option will search only empty files and directories. It does not need a value.

    find . -empty -type f

##### Filtering by File Name

The expression `-name <value>` filter files and directories by filename. Regular expressions are not allowed for the `<value>`, but shell patterns (also called *glob operators*) are permitted, such as `*`, `?`, or `[]`.

    find . -name '*.txt'
    find . -name 'image.jpg'

##### Filtering by File Path

The expression `-path <value>` filters files and directories by their file paths. Like `-name`, it does not accept regular expressions but shell patterns.

    find . -path '**/topdir1/*.jpg'
    
##### Filtering Using a Regex

File name matches regular expression *pattern* using `-regex <value>`. This is a match on the whole path, not a search. For example, to match a file named *./fubar*, you can use the regular expression `.*bar.` or `.*b.*3`, but not `f.*r3`

    find . -regex '.*1.txt'
    
The *positional option* `-regextype` can be used before `-regex`, to specify the regex engine you want to use. To output a list of regex engines supported, run `find . -regextype dummy`. Example output:

```
find: Unknown regular expression type ‘dummy’;
valid types are ‘findutils-default’, ‘ed’, ‘emacs’, ‘gnu-awk’, ‘grep’,
‘posix-awk’, ‘awk’, ‘posix-basic’, ‘posix-egrep’, ‘egrep’, ‘posix-extended’,
‘posix-minimal-basic’, ‘sed’.
```

The following example will find every text and jpg file using `egrep`, the extended regular expresion engine(ERE):

    find . -regextype "egrep" -regex '.*(txt|jpg)$'
    
##### Case insensitive search

Case-insensitive searches can be performed by adding the prefix `i` to the above
mentioned expressions. For example: `-iname`, `-ipath`, or `-iregex`.

##### Filtering by Type of File

The most common file types to filter on are:

  - `f` - File
  - `d` - Directory
  - `l` - Symbolic link

To search for more than one type at once, separate the options by a comma `,`.

    find . -name 'dir_a' -type d

##### Filtering by Permissions

Files can be filtered by whether they are `-executable`, `-readable`, or `writeable` for the current user. For additional granularity, you can use `-perm <value>`, where `<value>` can be:

  - A string beginning with `/` and followed by a series of rules using the **OR** boolean operator. For example, `-perm /u=w,g=e` (writable by the owner, *and* executable by the group).
  - A string beginning with `-` and followed by a series of rules using the **AND** boolean operator. For example, `-perm -u=w,g=e` (writable by owner, *or* executable by the group).
  - An octal number, for example: `644`.

##### Filtering by Owner or Group

  - `-user <value>` where `<value>` is a username.
  - `-group <value>` where `<value>` is a groupname.

---

#### Action Expressions

##### Deleting Files

Deleting files and directories can be accomplished using the `-delete` option.  The following command will delete all files and directories when their names begin with `test`.

    find . -name "test*" -delete
    
**WARNING**: This will permanently delete your files. Use with caution, if at all.

##### Running a Command on Each Result

The `-exec` expression *executes* a command. The string `{}` is replaced by the current file name being processed everywhere it occurs in the arguments to the command. All following arguments are taken to be arguments to the command until an argument consisting of `;` is encountered. Both of these constructions may need to be escaped with a backslash or quoted to protect them from expansion in the shell.


##### Running a Command in Working Directory

  - `find . -exec basename '{} ';'` - Run the command `basename` for every result of the search.
  - `find . -exec bash -c 'basename "${0%.*}"' '{}' \;` - The command `bash -c` will allow us to expand parameters. `${0%.*}` is used here to remove the file extension from each result.
  - `find . -name 'image.jpg' -exec file {} \;` - Run the `file` command against all `.jpg` files returned from the search.

You can also use the expression `-ok`. It is the same a the `-exec` option, except that find will prompt you, asking if you really want to run the command.  This confirmation will be asked for each result.

    find . -name "image.jpg" -ok file {} \;

##### Running a Command in Starting Directory

The two expressions `-execdir` and `-okdir` work like `-exec` and `-ok` respectively, except that the commands won’t run in your current working directory, but in the starting directory (the first argument of find).

    find topdir1/dir_b -exec bash -c 'basename "${0%*.}"' '{}' \;
    
Convert every jpg file in the `topdir1` directory, create new ones (in black & white) with the suffix "_bw.jpg".

    find topdir1 -name '*.jpg' -execdir bash -c 'convert $0 -colorspace Gray ${0%.*}_bw.jpg' {} ';'
    
Rename every jpg file in the `topdir1` directory with `_old` and keep same extension:

    find topdir1 -name "image.jpg" -type f -execdir rename 's/\.jpg$/_old.jpg/' {} \;
    
##### Changing the Output

The following options will change the output of the search results:

  - `-print` - This is the default action even when not specified. It simply prints every result.
  - `-ls` - Works like the regular `ls` command.
  - `-print0` - By default, the separator between different results is a `\n` newline character. With this option, the separator is a null character. Useful if you want to pipe results to `xargs -0`.
  - `-printf` - Output files with the information you need. For example: `find . -printf %d %p` will print the depth of the file in the file tree (`%d`) and the filename (`%p`).

##### Writing the Output to a File

You can also use a bunch of action expressions to write find’s output to a file. You just need to prefix the expression we saw above with a `f`. For example: `-fls`, `-fprint`, `-fprint0` or `-fprintf`. The value of these expressions will be the file written.


#### Operators

When no operators are explicitly specified, the `-and` operator is used
implicity between each expression.

  - `!` - Negate the expression following it.
  - `-or` or `-o` - Logical `OR`.
  - `-and` or `-a` - Logical `AND`.
  - `,` - Adding a comma is useful to use different sets of expressions while
  traversing the filesystem once.
  
  See the Examples section, below, for several use cases with operators.

---

### Examples

    * [Find command structure](#find-command-structure)
    * [Basic `find` file commands](#basic-`find`-file-commands)
    * [Case insensitive search](#case-insensitive-search)
    * [Search multiple dirs](#search-multiple-dirs)
    * [Files with different extensions](#files-with-different-extensions)
    * [Files that don't match a pattern (-not)](#files-that-don't-match-a-pattern-(-not))
    * [Files by text in the file (find + grep)](#files-by-text-in-the-file-(find-+-grep))
    * [5 lines before, 10 lines after grep matches](#5-lines-before,-10-lines-after-grep-matches)
    * [Files and act on them (find + exec)](#files-and-act-on-them-(find-+-exec))
    * [Find and copy](#find-and-copy)
    * [Copy one file to many directories](#copy-one-file-to-many-directories)
    * [Find and delete](#find-and-delete)
    * [Files by modification time](#files-by-modification-time)
    * [By modification time using a temp file](#by-modification-time-using-a-temp-file)
    * [find and tar](#find-and-tar)
    * [find, tar, and xargs](#find,-tar,-and-xargs)
    * [Rename](#rename)

The following examples make up the `find` command cookbook

#### Find command structure

Here is a basic example that decomposes a simple `find` command construct and
its respective elements:

    find topdir2 -name "myfile.txt" -perm 644
    
  - `topdir2` - the starting point of the search.
  - `-name` - A test expression.
  - `"myfile.txt"` - Value of the expression `-name`.
  - `-perm` - Another test expression.
  - `644` - The value of the expression `-perm`.

####  Basic `find` file commands

    find / -name foo.txt -type f -print             # full command
    find / -name foo.txt -type f                    # -print isn't necessary
    find / -name foo.txt                            # don't have to specify "type==file"
    find . -name foo.txt                            # search under the current dir
    find . -name "foo.*"                            # wildcard
    find . -name "*.txt"                            # wildcard
    find /users/al -name Cookbook -type d           # search '/users/al' dir

#### Case insensitive search

    find . -iname foo                               # find foo, Foo, FOo, FOO, etc.
    find . -iname foo -type d                       # same thing, but only dirs
    find . -iname foo -type f                       # same thing, but only files

#### Search multiple dirs

    find /opt /usr /var -name foo.scala -type f

#### Files with different extensions

    find . -type f \( -name "*.c" -o -name "*.sh" \) # "*.c" and "*.sh" files
    find . -type f \( -name "*cache" -o -name "*xml" -o -name "*html" \)   # three patterns

#### Files that don't match a pattern (-not)

    find . -type f -not -name "*.html"   # find all files not ending in ".html"

#### Files by text in the file (find + grep)

    find . -type f -name "*.java" -exec grep -l StringBuffer {} \;   # find StringBuffer in all *.java files
    find . -type f -name "*.java" -exec grep -il string {} \;  # ignore case with -i option
    find . -type f -name "*.gz" -exec zgrep 'GET /foo' {} \;   # search for a string in gzip'd files

#### 5 lines before, 10 lines after grep matches

    find . -type f -name "*.scala" -exec grep -B5 -A10 'null' {} \;

#### Files and act on them (find + exec)

    find /usr/local -name "*.html" -type f -exec chmod 644 {} \;   # change files to mode 644
    find htdocs cgi-bin -name "*.cgi" -type f -exec chmod 755 {} \;   # change files to mode 755
    find . -name "*.pl" -exec ls -ld {} \;   # run ls command on files found
    find . -type f -iname ".python-version" -print -exec sed -i 's/3.10.5/3.10.6/g' {} \;

#### Find and copy

    find . -type f -name "*.mp3" -exec cp {} ~/tmp/ \; # cp files to ~/tmp/

#### Copy one file to many directories

    find dir1 dir2 dir3 dir4 -type d -exec cp header.shtml {} \;    # copy file  to dirs

#### Find and delete

    find . -type f -name "Foo*" -exec rm {} \;   # remove "Foo*" files under current dir
    find . -type d -name CVS -exec rm -r {} \;   # remove subdirectories named "CVS" under current dir
    find . -name ".mediaartlocal" -type d -exec rm -r '{}' \; 

#### Files by modification time

    sudo find / -type f -mmin -10
    find . -mtime 1               # 24 hours
    find . -mtime -7              # last 7 days
    find . -mtime -7 -type f      # just files
    find . -mtime -7 -type d      # just dirs
    
#### By modification time using a temp file

    touch 09301330 foo   # 1) create a temp file with a specific timestamp
    find . -mnewer foo   # 2) returns a list of new files
    rm foo               # 3) rm the temp file

#### find and tar

    find . -type f -name "*.java" | xargs tar cvf myfile.tar
    find . -type f -name "*.java" | xargs tar rvf myfile.tar

#### find, tar, and xargs

    find . -name -type f '*.mp3' -mtime -180 -print0 | xargs -0 tar rvf music.tar

     (-print0 helps handle spaces in filenames)

#### Rename

    find . -name "folder.jpg" -type f -execdir mv {} cover.jpg \;
    find ~ -iname "*new*" -exec mv -v '{}' /media/current-projects/ \;

---

### Resources

Most the information & examples provided above were originally sourced from the following resources:

  - [Linux man page - find](https://manned.org/find)
  - [Alvin Alexander - find](https://alvinalexander.com/unix/edu/examples/find.shtml)
  - [The Mouseless Dev](https://themouseless.dev/posts/find-guide-example-mouseless/)
