# docstring-in-stub (PYI021)
Derived from the flake8-pyi linter.
Fix is always available.
## What it does
Checks for the presence of docstrings in stub files.
## Why is this bad?
Stub files should omit docstrings, as they're intended to provide type
hints, rather than documentation.
## Example
```
def func(param: int) -> str:
    """This is a docstring."""
    ...
```
## Use instead:
```
def func(param: int) -> str: ...
```