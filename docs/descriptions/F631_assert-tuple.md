# assert-tuple (F631)
Derived from the Pyflakes linter.
## What it does
Checks for assert statements that use non-empty tuples as test
conditions.
## Why is this bad?
Non-empty tuples are always True, so an assert statement with a
non-empty tuple as its test condition will always pass. This is likely a
mistake.
## Example
```
assert (some_condition,)
```
## Use instead:
```
assert some_condition
```