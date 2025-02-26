# pass-in-class-body (PYI012)
Derived from the flake8-pyi linter.
Fix is always available.
## What it does
Checks for the presence of the pass statement in non-empty class bodies
in .pyi files.
## Why is this bad?
The pass statement is always unnecessary in non-empty class bodies in
stubs.
## Example
```
class MyClass:
    x: int
    pass
```
## Use instead:
```
class MyClass:
    x: int
```