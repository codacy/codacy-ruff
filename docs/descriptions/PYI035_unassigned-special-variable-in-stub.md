# unassigned-special-variable-in-stub (PYI035)
Derived from the flake8-pyi linter.
## What it does
Checks that __all__, __match_args__, and __slots__ variables are
assigned to values when defined in stub files.
## Why is this bad?
Special variables like __all__ have the same semantics in stub files
as they do in Python modules, and so should be consistent with their
runtime counterparts.
## Example
```
__all__: list[str]
```
## Use instead:
```
__all__: list[str] = ["foo", "bar"]
```