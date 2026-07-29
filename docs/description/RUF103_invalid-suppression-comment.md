# invalid-suppression-comment (RUF103)
Added in 0.15.0 ·
Related issues ·
View source
Fix is always available.
## What it does
Checks for invalid suppression comments
## Why is this bad?
Invalid suppression comments are ignored by Ruff, and should either
be fixed or removed to avoid confusion.
## Example
```
# ruff: disable  # missing codes
```
## Use instead:
```
# ruff: disable[E501]
Or delete the invalid suppression comment.
```