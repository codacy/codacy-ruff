# shebang-missing-executable-file (EXE002)
Derived from the flake8-executable linter.
## What it does
Checks for executable .py files that do not have a shebang.
## Why is this bad?
In Python, a shebang (also known as a hashbang) is the first line of a
script, which specifies the interpreter that should be used to run the
script.
If a .py file is executable, but does not have a shebang, it may be run
with the wrong interpreter, or fail to run at all.
If the file is meant to be executable, add a shebang, as in:
#!/usr/bin/env python
Otherwise, remove the executable bit from the file
(e.g., chmod -x __main__.py or git update-index --chmod=-x __main__.py).
A file is considered executable if it has the executable bit set (i.e., its
permissions mode intersects with 0o111). As such, this rule is only
available on Unix-like systems, and is not enforced on Windows or WSL.
```