# over-indentation (D208)
Derived from the pydocstyle linter.
Fix is always available.
## What it does
Checks for over-indented docstrings.
## Why is this bad?
PEP 257 recommends that docstrings be indented to the same level as their
opening quotes. Avoid over-indenting docstrings, for consistency.
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
    """Return a sorted copy of the list.
    Sort the list in ascending order and return a copy of the result using the bubble
    sort algorithm.
    """
Formatter compatibility
We recommend against using this rule alongside the formatter. The
formatter enforces consistent indentation, making the rule redundant.
```