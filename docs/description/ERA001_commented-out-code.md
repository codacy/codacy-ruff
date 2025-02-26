# commented-out-code (ERA001)
Derived from the eradicate linter.
## What it does
Checks for commented-out Python code.
## Why is this bad?
Commented-out code is dead code, and is often included inadvertently.
It should be removed.
Known problems
Prone to false positives when checking comments that resemble Python code,
but are not actually Python code (#4845).
## Example
```
# print("Hello, world!")
```