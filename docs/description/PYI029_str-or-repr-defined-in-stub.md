# str-or-repr-defined-in-stub (PYI029)
Derived from the flake8-pyi linter.
Fix is always available.
## What it does
Checks for redundant definitions of __str__ or __repr__ in stubs.
## Why is this bad?
Defining __str__ or __repr__ in a stub is almost always redundant,
as the signatures are almost always identical to those of the default
equivalent, object.__str__ and object.__repr__, respectively.
## Example
```
class Foo:
    def __repr__(self) -> str: ...
```