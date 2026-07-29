# open-alias (UP020)
Added in v0.0.196 ·
Related issues ·
View source
Derived from the pyupgrade linter.
Fix is sometimes available.
## What it does
Checks for uses of io.open.
## Why is this bad?
In Python 3, io.open is an alias for open. Prefer using open directly,
as it is more idiomatic.
## Example
```
import io
with io.open("file.txt") as f:
    ...
```
## Use instead:
```
with open("file.txt") as f:
    ...
Fix safety
This rule's fix is marked as safe, unless the expression contains comments.
```