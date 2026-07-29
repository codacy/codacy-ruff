# ellipsis-in-non-empty-class-body (PYI013)
Added in v0.0.270 ·
Related issues ·
View source
Derived from the flake8-pyi linter.
Fix is always available.
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