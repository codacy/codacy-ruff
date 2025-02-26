# native-literals (UP018)
Derived from the pyupgrade linter.
Fix is always available.
## What it does
Checks for unnecessary calls to str, bytes, int, float, and bool.
## Why is this bad?
The mentioned constructors can be replaced with their respective literal
forms, which are more readable and idiomatic.
## Example
```
str("foo")
```
## Use instead:
```
"foo"
Fix safety
The fix is marked as unsafe if it might remove comments.
```