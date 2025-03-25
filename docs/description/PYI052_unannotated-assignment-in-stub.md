# unannotated-assignment-in-stub (PYI052)
Derived from the flake8-pyi linter.
## What it does
Checks for unannotated assignments in stub (.pyi) files.
## Why is this bad?
Stub files exist to provide type hints, and are never executed. As such,
all assignments in stub files should be annotated with a type.
```