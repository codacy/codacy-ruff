# stub-body-multiple-statements (PYI048)
Derived from the flake8-pyi linter.
## What it does
Checks for functions in stub (.pyi) files that contain multiple
statements.
## Why is this bad?
Stub files are never executed, and are only intended to define type hints.
As such, functions in stub files should not contain functional code, and
should instead contain only a single statement (e.g., ...).
## Example
```
def function():
    x = 1
    y = 2
    return x + y
```
## Use instead:
```
def function(): ...
```