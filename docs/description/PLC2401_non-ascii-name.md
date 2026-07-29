# non-ascii-name (PLC2401)
Added in 0.5.0 ·
Related issues ·
View source
Derived from the Pylint linter.
## What it does
Checks for the use of non-ASCII characters in variable names.
## Why is this bad?
The use of non-ASCII characters in variable names can cause confusion
and compatibility issues (see: PEP 672).
## Example
```
ápple_count: int
```
## Use instead:
```
apple_count: int
```