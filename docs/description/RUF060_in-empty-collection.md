# in-empty-collection (RUF060)
Added in 0.15.0 ·
Related issues ·
View source
## What it does
Checks for membership tests on empty collections (such as list, tuple, set, or dict).
## Why is this bad?
If the collection is always empty, the check is unnecessary and can be removed.
## Example
```
if 1 not in set():
    print("got it!")
```
## Use instead:
```
print("got it!")
```