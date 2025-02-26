# quoted-annotation-in-stub (PYI020)
Derived from the flake8-pyi linter.
Fix is always available.
## What it does
Checks for quoted type annotations in stub (.pyi) files, which should be avoided.
## Why is this bad?
Stub files natively support forward references in all contexts, as stubs
are never executed at runtime. (They should be thought of as "data files"
for type checkers and IDEs.) As such, quotes are never required for type
annotations in stub files, and should be omitted.
## Example
```
def function() -> "int": ...
```
## Use instead:
```
def function() -> int: ...
```