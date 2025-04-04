# assignment-default-in-stub (PYI015)
Derived from the flake8-pyi linter.
Fix is always available.
## What it does
Checks for assignments in stubs with default values that are not "simple"
(i.e., int, float, complex, bytes, str, bool, None, ..., or
simple container literals).
## Why is this bad?
Stub (.pyi) files exist to define type hints, and are not evaluated at
runtime. As such, assignments in stub files should not include values,
as they are ignored by type checkers.
However, the use of such values may be useful for IDEs and other consumers
of stub files, and so "simple" values may be worth including and are
permitted by this rule.
Instead of including and reproducing a complex value, use ... to indicate
that the assignment has a default value, but that the value is non-simple
or varies according to the current platform or Python version.
## Example
```
foo: str = "..."
```
## Use instead:
```
foo: str = ...
```