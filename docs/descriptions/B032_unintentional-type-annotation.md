# unintentional-type-annotation (B032)
Derived from the flake8-bugbear linter.
## What it does
Checks for the unintentional use of type annotations.
## Why is this bad?
The use of a colon (:) in lieu of an assignment (=) can be syntactically valid, but
is almost certainly a mistake when used in a subscript or attribute assignment.
## Example
```
a["b"]: 1
```
## Use instead:
```
a["b"] = 1
```