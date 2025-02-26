# missing-terminal-punctuation (D415)
Derived from the pydocstyle linter.
Fix is sometimes available.
## What it does
Checks for docstrings in which the first line does not end in a punctuation
mark, such as a period, question mark, or exclamation point.
## Why is this bad?
The first line of a docstring should end with a period, question mark, or
exclamation point, for grammatical correctness and consistency.
This rule may not apply to all projects; its applicability is a matter of
convention. By default, this rule is enabled when using the google
convention, and disabled when using the numpy and pep257 conventions.
## Example
```
def average(values: list[float]) -> float:
    """Return the mean of the given values"""
```
## Use instead:
```
def average(values: list[float]) -> float:
    """Return the mean of the given values."""
```