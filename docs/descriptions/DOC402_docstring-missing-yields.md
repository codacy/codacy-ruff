# docstring-missing-yields (DOC402)
Derived from the pydoclint linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for functions with yield statements that do not have "Yields" sections in
their docstrings.
## Why is this bad?
A missing "Yields" section is a sign of incomplete documentation.
This rule is not enforced for abstract methods or functions that only yield None.
It is also ignored for "stub functions": functions where the body only consists
of pass, ..., raise NotImplementedError, or similar.
## Example
```
def count_to_n(n: int) -> int:
    """Generate integers up to *n*.
    Args:
        n: The number at which to stop counting.
    """
    for i in range(1, n + 1):
        yield i
```
## Use instead:
```
def count_to_n(n: int) -> int:
    """Generate integers up to *n*.
    Args:
        n: The number at which to stop counting.
    Yields:
        int: The number we're at in the count.
    """
    for i in range(1, n + 1):
        yield i
```