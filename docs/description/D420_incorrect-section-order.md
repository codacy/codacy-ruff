# incorrect-section-order (D420)
Preview (since 0.15.3) ·
Related issues ·
View source
Derived from the pydocstyle linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for docstring sections that appear out of order.
## Why is this bad?
Docstring sections should follow the canonical ordering specified by the
docstring convention (NumPy or Google). Consistent ordering makes
docstrings easier to read and navigate.
For the NumPy convention, all sections have a prescribed order per the
numpydoc style guide. For the Google convention, only the relative ordering
of Args, Returns/Yields, and Raises is enforced; all other sections
are unordered.
## Example
```
Given lint.pydocstyle.convention = "numpy":
def func() -> int:
    """Summary.
    Notes
    -----
    Some notes.
    Returns
    -------
    int
    """
```
## Use instead:
```
def func() -> int:
    """Summary.
    Returns
    -------
    int
    Notes
    -----
    Some notes.
    """
Given lint.pydocstyle.convention = "google":
def func(x: int) -> int:
    """Summary.
    Returns:
        int
    Args:
        x: Description.
    """
```
## Use instead:
```
def func(x: int) -> int:
    """Summary.
    Args:
        x: Description.
    Returns:
        int
    """
```