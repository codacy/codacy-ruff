# shebang-missing-python (EXE003)
Derived from the flake8-executable linter.
## What it does
Checks for a shebang directive in .py files that does not contain python,
pytest, or uv run.
## Why is this bad?
In Python, a shebang (also known as a hashbang) is the first line of a
script, which specifies the command that should be used to run the
script.
For Python scripts, if the shebang does not include a command that explicitly
or implicitly specifies an interpreter, then the file will be executed with
the default interpreter, which is likely a mistake.
## Example
```
#!/usr/bin/env bash
```
## Use instead:
```
#!/usr/bin/env python3
```