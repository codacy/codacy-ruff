# multi-line-summary-second-line (D213)
Derived from the pydocstyle linter.
Fix is always available.
## What it does
Checks for docstring summary lines that are not positioned on the second
physical line of the docstring.
## Why is this bad?
PEP 257 recommends that multi-line docstrings consist of "a summary line
just like a one-line docstring, followed by a blank line, followed by a
more elaborate description."
The summary line should be located on the second physical line of the
docstring, immediately after the opening quotes and the blank line.
This rule may not apply to all projects; its applicability is a matter of
convention. By default, this rule is disabled when using the google,
numpy, and pep257 conventions.
For an alternative, see D212.
## Example
```
def sort_list(l: list[int]) -> list[int]:
    """Return a sorted copy of the list.
    Sort the list in ascending order and return a copy of the result using the
    bubble sort algorithm.
    """
```
## Use instead:
```
def sort_list(l: list[int]) -> list[int]:
    """
    Return a sorted copy of the list.
    Sort the list in ascending order and return a copy of the result using the bubble
    sort algorithm.
    """
```