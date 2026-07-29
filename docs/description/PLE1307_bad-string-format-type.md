# bad-string-format-type (PLE1307)
Added in v0.0.245 ·
Related issues ·
View source
Derived from the Pylint linter.
## What it does
Checks for mismatched argument types in "old-style" format strings.
## Why is this bad?
The format string is not checked at compile time, so it is easy to
introduce bugs by mistyping the format string.
## Example
```
print("%d" % "1")
```
## Use instead:
```
print("%d" % 1)
```