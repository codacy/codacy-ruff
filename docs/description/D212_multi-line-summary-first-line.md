# multi-line-summary-first-line (D212)
Derived from the pydocstyle linter.
Fix is always available.
## What it does
Checks for docstring summary lines that are not positioned on the first
physical line of the docstring.
## Why is this bad?
PEP 257 recommends that multi-line docstrings consist of "a summary line
just like a one-line docstring, followed by a blank line, followed by a
more elaborate description."
The summary line should be located on the first physical line of the
docstring, immediately after the opening quotes.
This rule may not apply to all projects; its applicability is a matter of
convention. By default, this rule is enabled when using the google
convention, and disabled when using the numpy and pep257 conventions.
For an alternative, see D213.
## Example
```
def sort_list(l: list[int]) -> list[int]:
    """
    Return a sorted copy of the list.
    Sort the list in ascending order and return a copy of the result using the
    bubble sort algorithm.
    """
```
## Use instead:
```
def sort_list(l: list[int]) -> list[int]:
    """Return a sorted copy of the list.
    Sort the list in ascending order and return a copy of the result using the bubble
    sort algorithm.
    """
```