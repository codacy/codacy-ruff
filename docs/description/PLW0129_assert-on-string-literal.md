# assert-on-string-literal (PLW0129)
Derived from the Pylint linter.
## What it does
Checks for assert statements that use a string literal as the first
argument.
## Why is this bad?
An assert on a non-empty string literal will always pass, while an
assert on an empty string literal will always fail.
## Example
```
assert "always true"
```