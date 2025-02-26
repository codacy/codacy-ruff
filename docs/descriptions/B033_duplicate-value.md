# duplicate-value (B033)
Derived from the flake8-bugbear linter.
Fix is sometimes available.
## What it does
Checks for set literals that contain duplicate items.
## Why is this bad?
In Python, sets are unordered collections of unique elements. Including a
duplicate item in a set literal is redundant, as the duplicate item will be
replaced with a single item at runtime.
## Example
```
{1, 2, 3, 1}
```
## Use instead:
```
{1, 2, 3}
```