# future-annotations-in-stub (PYI044)
Derived from the flake8-pyi linter.
Fix is sometimes available.
## What it does
Checks for the presence of the from __future__ import annotations import
statement in stub files.
## Why is this bad?
Stub files natively support forward references in all contexts, as stubs are
never executed at runtime. (They should be thought of as "data files" for
type checkers.) As such, the from __future__ import annotations import
statement has no effect and should be omitted.
```