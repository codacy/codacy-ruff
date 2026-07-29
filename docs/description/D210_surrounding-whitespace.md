# surrounding-whitespace (D210)
Added in v0.0.68 ·
Related issues ·
View source
Derived from the pydocstyle linter.
Fix is sometimes available.
## What it does
Checks for surrounding whitespace in docstrings.
## Why is this bad?
Remove surrounding whitespace from the docstring, for consistency.
## Example
```
def factorial(n: int) -> int:
    """ Return the factorial of n. """
```
## Use instead:
```
def factorial(n: int) -> int:
    """Return the factorial of n."""
```