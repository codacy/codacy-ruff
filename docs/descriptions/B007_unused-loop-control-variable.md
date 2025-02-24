# unused-loop-control-variable (B007)
Derived from the flake8-bugbear linter.
Fix is sometimes available.
## What it does
Checks for unused variables in loops (e.g., for and while statements).
## Why is this bad?
Defining a variable in a loop statement that is never used can confuse
readers.
If the variable is intended to be unused (e.g., to facilitate
destructuring of a tuple or other object), prefix it with an underscore
to indicate the intent. Otherwise, remove the variable entirely.
## Example
```
for i, j in foo:
    bar(i)
```
## Use instead:
```
for i, _j in foo:
    bar(i)
```