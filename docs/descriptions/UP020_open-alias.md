# open-alias (UP020)
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
```