# pass-statement-stub-body (PYI009)
Derived from the flake8-pyi linter.
Fix is always available.
## What it does
Checks for pass statements in empty stub bodies.
## Why is this bad?
For stylistic consistency, ... should always be used rather than pass
in stub files.
## Example
```
def foo(bar: int) -> list[int]: pass
```
## Use instead:
```
def foo(bar: int) -> list[int]: ...
```