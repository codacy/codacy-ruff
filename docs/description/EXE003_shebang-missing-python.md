# shebang-missing-python (EXE003)
Derived from the flake8-executable linter.
## What it does
Checks for a shebang directive in .py files that does not contain python.
## Why is this bad?
In Python, a shebang (also known as a hashbang) is the first line of a
script, which specifies the interpreter that should be used to run the
script.
For Python scripts, the shebang must contain python to indicate that the
script should be executed as a Python script. If the shebang does not
contain python, then the file will be executed with the default
interpreter, which is likely a mistake.
## Example
```
#!/usr/bin/env bash
```
## Use instead:
```
#!/usr/bin/env python3
```