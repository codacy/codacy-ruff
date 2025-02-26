# f-string-docstring (B021)
Derived from the flake8-bugbear linter.
## What it does
Checks for docstrings that are written via f-strings.
## Why is this bad?
Python will interpret the f-string as a joined string, rather than as a
docstring. As such, the "docstring" will not be accessible via the
__doc__ attribute, nor will it be picked up by any automated
documentation tooling.
## Example
```
def foo():
    f"""Not a docstring."""
```
## Use instead:
```
def foo():
    """A docstring."""
```