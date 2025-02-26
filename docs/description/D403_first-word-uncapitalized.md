# first-word-uncapitalized (D403)
Derived from the pydocstyle linter.
Fix is always available.
## What it does
Checks for docstrings that do not start with a capital letter.
## Why is this bad?
The first non-whitespace character in a docstring should be
capitalized for grammatical correctness and consistency.
## Example
```
def average(values: list[float]) -> float:
    """return the mean of the given values."""
```
## Use instead:
```
def average(values: list[float]) -> float:
    """Return the mean of the given values."""
```