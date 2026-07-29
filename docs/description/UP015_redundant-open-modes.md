# redundant-open-modes (UP015)
Added in v0.0.155 ·
Related issues ·
View source
Derived from the pyupgrade linter.
Fix is always available.
## What it does
Checks for redundant open mode arguments.
## Why is this bad?
Redundant open mode arguments are unnecessary and should be removed to
avoid confusion.
## Example
```
with open("foo.txt", "r") as f:
    ...
```
## Use instead:
```
with open("foo.txt") as f:
    ...
```