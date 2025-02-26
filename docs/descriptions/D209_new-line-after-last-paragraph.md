# new-line-after-last-paragraph (D209)
Derived from the pydocstyle linter.
Fix is always available.
## What it does
Checks for multi-line docstrings whose closing quotes are not on their
own line.
## Why is this bad?
PEP 257 recommends that the closing quotes of a multi-line docstring be
on their own line, for consistency and compatibility with documentation
tools that may need to parse the docstring.
## Example
```
def sort_list(l: List[int]) -> List[int]:
    """Return a sorted copy of the list.
    Sort the list in ascending order and return a copy of the result using the
    bubble sort algorithm."""
```
## Use instead:
```
def sort_list(l: List[int]) -> List[int]:
    """Return a sorted copy of the list.
    Sort the list in ascending order and return a copy of the result using the bubble
    sort algorithm.
    """
```