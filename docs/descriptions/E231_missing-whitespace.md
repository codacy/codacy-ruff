# missing-whitespace (E231)
Derived from the pycodestyle linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for missing whitespace after ,, ;, and :.
## Why is this bad?
Missing whitespace after ,, ;, and : makes the code harder to read.
## Example
```
a = (1,2)
```
## Use instead:
```
a = (1, 2)
```