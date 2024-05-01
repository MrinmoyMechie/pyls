# pyls: Python Equivalent of ls Command
pyls is a Python implementation of the ls command, providing similar functionality along with additional options.

# Installation
To install pyls, clone this repository:
https://github.com/MrinmoyMechie/pyls.git
then you can run "pip install -e ." from commandline to add pyls in your system

# Usage
Once installed, you can use pyls in your terminal. The basic usage is:
pyls [options]

# Options
-A: Include hidden files and directories.
-l: Display in long format.
-r: Display in reverse order.
-t: Sort by modification time.
--filter=<>: Filter files or directories based on your preference, "file" for filtering files and "dir" for directories.
-h: Display file sizes in human-readable format.
--help: Display help message.

## List all files and directories in the current directory
pyls

## List all files and directories including hidden ones
pyls -A

## List files and directories in long list format
pyls -l

## List files and directories in reverse order
pyls -r

## List files and directories sorted by modification time in ascending order
pyls -t

## Filter files and directories within a directory
pyls --filter=" ";  use either dir or file

## Display file sizes in human-readable format
pyls -h

## Display help message
pyls --help

# Contributing
Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.
