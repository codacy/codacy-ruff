# no-indented-block (E112)
Derived from the pycodestyle linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for indented blocks that are lacking indentation.
## Why is this bad?
All indented blocks should be indented; otherwise, they are not valid
Python syntax.
## Example
```
for item in items:
pass
```
## Use instead:
```
for item in items:
    pass
```