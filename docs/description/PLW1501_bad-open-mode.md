# bad-open-mode (PLW1501)
Derived from the Pylint linter.
## What it does
Check for an invalid mode argument in open calls.
## Why is this bad?
The open function accepts a mode argument that specifies how the file
should be opened (e.g., read-only, write-only, append-only, etc.).
Python supports a variety of open modes: r, w, a, and x, to control
reading, writing, appending, and creating, respectively, along with
b (binary mode), + (read and write), and U (universal newlines),
the latter of which is only valid alongside r. This rule detects both
invalid combinations of modes and invalid characters in the mode string
itself.
## Example
```
with open("file", "rwx") as f:
    return f.read()
```
## Use instead:
```
with open("file", "r") as f:
    return f.read()
```