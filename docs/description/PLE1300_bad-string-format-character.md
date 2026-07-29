# bad-string-format-character (PLE1300)
Added in v0.0.283 ·
Related issues ·
View source
Derived from the Pylint linter.
## What it does
Checks for unsupported format types in format strings.
## Why is this bad?
An invalid format string character will result in an error at runtime.
## Example
```
# `z` is not a valid format type.
print("%z" % "1")
print("{:z}".format("1"))
```