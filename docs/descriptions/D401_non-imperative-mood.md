# non-imperative-mood (D401)
Derived from the pydocstyle linter.
## What it does
Checks for docstring first lines that are not in an imperative mood.
## Why is this bad?
PEP 257 recommends that the first line of a docstring be written in the
imperative mood, for consistency.
Hint: to rewrite the docstring in the imperative, phrase the first line as
if it were a command.
This rule may not apply to all projects; its applicability is a matter of
convention. By default, this rule is enabled when using the numpy and
pep257 conventions, and disabled when using the google conventions.
## Example
```
def average(values: list[float]) -> float:
    """Returns the mean of the given values."""
```
## Use instead:
```
def average(values: list[float]) -> float:
    """Return the mean of the given values."""
```