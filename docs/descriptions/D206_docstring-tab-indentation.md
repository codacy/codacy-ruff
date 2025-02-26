# docstring-tab-indentation (D206)
Derived from the pydocstyle linter.
## What it does
Checks for docstrings that are indented with tabs.
## Why is this bad?
PEP 8 recommends using spaces over tabs for indentation.
## Example
```
def sort_list(l: list[int]) -> list[int]:
    """Return a sorted copy of the list.
    Sort the list in ascending order and return a copy of the result using the bubble
    sort algorithm.
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
The rule is also incompatible with the formatter when using
format.indent-style="tab".
```