# readlines-in-for (FURB129)
Derived from the refurb linter.
Fix is always available.
## What it does
Checks for uses of readlines() when iterating over a file line-by-line.
## Why is this bad?
Rather than iterating over all lines in a file by calling readlines(),
it's more convenient and performant to iterate over the file object
directly.
## Example
```
with open("file.txt") as fp:
    for line in fp.readlines():
        ...
```
## Use instead:
```
with open("file.txt") as fp:
    for line in fp:
        ...
```