# yoda-conditions (SIM300)
Derived from the flake8-simplify linter.
Fix is sometimes available.
## What it does
Checks for conditions that position a constant on the left-hand side of the
comparison operator, rather than the right-hand side.
## Why is this bad?
These conditions (sometimes referred to as "Yoda conditions") are less
readable than conditions that place the variable on the left-hand side of
the comparison operator.
In some languages, Yoda conditions are used to prevent accidental
assignment in conditions (i.e., accidental uses of the = operator,
instead of the == operator). However, Python does not allow assignments
in conditions unless using the := operator, so Yoda conditions provide
no benefit in this regard.
## Example
```
if "Foo" == foo:
    ...
```
## Use instead:
```
if foo == "Foo":
    ...
```