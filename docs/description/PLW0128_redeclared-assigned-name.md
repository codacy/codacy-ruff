# redeclared-assigned-name (PLW0128)
Derived from the Pylint linter.
## What it does
Checks for declared assignments to the same variable multiple times
in the same assignment.
## Why is this bad?
Assigning a variable multiple times in the same assignment is redundant,
as the final assignment to the variable is what the value will be.
## Example
```
a, b, a = (1, 2, 3)
print(a)  # 3
```
## Use instead:
```
# this is assuming you want to assign 3 to `a`
_, b, a = (1, 2, 3)
print(a)  # 3
```