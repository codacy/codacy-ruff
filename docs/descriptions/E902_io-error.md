# io-error (E902)
Derived from the pycodestyle linter.
## What it does
This is not a regular diagnostic; instead, it's raised when a file cannot be read
from disk.
## Why is this bad?
An IOError indicates an error in the development setup. For example, the user may
not have permissions to read a given file, or the filesystem may contain a broken
symlink.
## Example
```
On Linux or macOS:
$ echo 'print("hello world!")' > a.py
$ chmod 000 a.py
$ ruff a.py
a.py:1:1: E902 Permission denied (os error 13)
Found 1 error.
```