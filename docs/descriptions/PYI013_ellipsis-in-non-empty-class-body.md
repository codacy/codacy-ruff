# ellipsis-in-non-empty-class-body (PYI013)
Derived from the flake8-pyi linter.
Fix is sometimes available.
## What it does
Removes ellipses (...) in otherwise non-empty class bodies.
## Why is this bad?
An ellipsis in a class body is only necessary if the class body is
otherwise empty. If the class body is non-empty, then the ellipsis
is redundant.
## Example
```
class Foo:
    ...
    value: int
```
## Use instead:
```
class Foo:
    value: int
```