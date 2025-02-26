# signature-in-docstring (D402)
Derived from the pydocstyle linter.
## What it does
Checks for function docstrings that include the function's signature in
the summary line.
## Why is this bad?
PEP 257 recommends against including a function's signature in its
docstring. Instead, consider using type annotations as a form of
documentation for the function's parameters and return value.
This rule may not apply to all projects; its applicability is a matter of
convention. By default, this rule is enabled when using the google and
pep257 conventions, and disabled when using the numpy convention.
## Example
```
def foo(a, b):
    """foo(a: int, b: int) -> list[int]"""
```
## Use instead:
```
def foo(a: int, b: int) -> list[int]:
    """Return a list of a and b."""
```