# shebang-not-first-line (EXE005)
Derived from the flake8-executable linter.
## What it does
Checks for a shebang directive that is not at the beginning of the file.
## Why is this bad?
In Python, a shebang (also known as a hashbang) is the first line of a
script, which specifies the interpreter that should be used to run the
script.
The shebang's #! prefix must be the first two characters of a file. If
the shebang is not at the beginning of the file, it will be ignored, which
is likely a mistake.
## Example
```
foo = 1
#!/usr/bin/env python3
```
## Use instead:
```
#!/usr/bin/env python3
foo = 1
```