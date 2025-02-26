# argument-default-in-stub (PYI014)
Derived from the flake8-pyi linter.
Fix is always available.
## What it does
Checks for untyped function arguments in stubs with default values that
are not "simple" /// (i.e., int, float, complex, bytes, str,
bool, None, ..., or simple container literals).
## Why is this bad?
Stub (.pyi) files exist to define type hints, and are not evaluated at
runtime. As such, function arguments in stub files should not have default
values, as they are ignored by type checkers.
However, the use of default values may be useful for IDEs and other
consumers of stub files, and so "simple" values may be worth including and
are permitted by this rule.
Instead of including and reproducing a complex value, use ... to indicate
that the assignment has a default value, but that the value is non-simple
or varies according to the current platform or Python version.
## Example
```
def foo(arg=[]) -> None: ...
```
## Use instead:
```
def foo(arg=...) -> None: ...
```