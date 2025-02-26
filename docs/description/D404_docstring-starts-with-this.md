# docstring-starts-with-this (D404)
Derived from the pydocstyle linter.
## What it does
Checks for docstrings that start with This.
## Why is this bad?
PEP 257 recommends that the first line of a docstring be written in the
imperative mood, for consistency.
Hint: to rewrite the docstring in the imperative, phrase the first line as
if it were a command.
This rule may not apply to all projects; its applicability is a matter of
convention. By default, this rule is enabled when using the numpy
convention,, and disabled when using the google and pep257 conventions.
## Example
```
def average(values: list[float]) -> float:
    """This function returns the mean of the given values."""
```
## Use instead:
```
def average(values: list[float]) -> float:
    """Return the mean of the given values."""
```