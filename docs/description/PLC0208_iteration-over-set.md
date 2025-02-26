# iteration-over-set (PLC0208)
Derived from the Pylint linter.
Fix is always available.
## What it does
Checks for iteration over a set literal where each element in the set is
itself a literal value.
## Why is this bad?
Iterating over a set is less efficient than iterating over a sequence
type, like list or tuple.
## Example
```
for number in {1, 2, 3}:
    ...
```
## Use instead:
```
for number in (1, 2, 3):
    ...
```