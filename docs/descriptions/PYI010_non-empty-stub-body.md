# non-empty-stub-body (PYI010)
Derived from the flake8-pyi linter.
Fix is always available.
## What it does
Checks for non-empty function stub bodies.
## Why is this bad?
Stub files are never executed at runtime; they should be thought of as
"data files" for type checkers or IDEs. Function bodies are redundant
for this purpose.
## Example
```
def double(x: int) -> int:
    return x * 2
```
## Use instead:
```
def double(x: int) -> int: ...
```