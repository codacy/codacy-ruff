# iteration-over-set (PLC0208)
Added in v0.0.271 ·
Related issues ·
View source
Derived from the Pylint linter.
Fix is always available.
## What it does
Checks for iteration over a set literal in which each element is a literal.
## Why is this bad?
Iterating over a set is less efficient than iterating over a sequence
type, such as list or tuple.
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