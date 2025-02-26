# open-file-with-context-handler (SIM115)
Derived from the flake8-simplify linter.
## What it does
Checks for cases where files are opened (e.g., using the builtin open() function)
without using a context manager.
## Why is this bad?
If a file is opened without a context manager, it is not guaranteed that
the file will be closed (e.g., if an exception is raised), which can cause
resource leaks. The rule detects a wide array of IO calls where context managers
could be used, such as open, pathlib.Path(...).open(), tempfile.TemporaryFile()
ortarfile.TarFile(...).gzopen().
## Example
```
file = open("foo.txt")
...
file.close()
```
## Use instead:
```
with open("foo.txt") as file:
    ...
```