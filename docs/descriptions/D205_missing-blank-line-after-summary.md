# missing-blank-line-after-summary (D205)
Derived from the pydocstyle linter.
Fix is sometimes available.
## What it does
Checks for docstring summary lines that are not separated from the docstring
description by one blank line.
## Why is this bad?
PEP 257 recommends that multi-line docstrings consist of "a summary line
just like a one-line docstring, followed by a blank line, followed by a
more elaborate description."
## Example
```
def sort_list(l: list[int]) -> list[int]:
    """Return a sorted copy of the list.
    Sort the list in ascending order and return a copy of the
    result using the bubble sort algorithm.
    """
```
## Use instead:
```
def sort_list(l: list[int]) -> list[int]:
    """Return a sorted copy of the list.
    Sort the list in ascending order and return a copy of the
    result using the bubble sort algorithm.
    """
```