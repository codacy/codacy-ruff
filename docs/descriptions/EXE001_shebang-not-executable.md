# shebang-not-executable (EXE001)
Derived from the flake8-executable linter.
## What it does
Checks for a shebang directive in a file that is not executable.
## Why is this bad?
In Python, a shebang (also known as a hashbang) is the first line of a
script, which specifies the interpreter that should be used to run the
script.
The presence of a shebang suggests that a file is intended to be
executable. If a file contains a shebang but is not executable, then the
shebang is misleading, or the file is missing the executable bit.
If the file is meant to be executable, add the executable bit to the file
(e.g., chmod +x __main__.py or git update-index --chmod=+x __main__.py).
Otherwise, remove the shebang.
A file is considered executable if it has the executable bit set (i.e., its
permissions mode intersects with 0o111). As such, this rule is only
available on Unix-like systems, and is not enforced on Windows or WSL.
## Example
```
#!/usr/bin/env python
```