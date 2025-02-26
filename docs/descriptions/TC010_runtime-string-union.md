# runtime-string-union (TC010)
Derived from the flake8-type-checking linter.
## What it does
Checks for the presence of string literals in X | Y-style union types.
## Why is this bad?
PEP 604 introduced a new syntax for union type annotations based on the
| operator.
While Python's type annotations can typically be wrapped in strings to
avoid runtime evaluation, the use of a string member within an X | Y-style
union type will cause a runtime error.
Instead, remove the quotes, wrap the entire union in quotes, or use
from __future__ import annotations to disable runtime evaluation of
annotations entirely.
## Example
```
var: str | "int"
```
## Use instead:
```
var: str | int
Or, extend the quotes to include the entire union:
var: "str | int"
```