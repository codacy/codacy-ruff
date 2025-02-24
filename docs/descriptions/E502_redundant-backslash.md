# redundant-backslash (E502)
Derived from the pycodestyle linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for redundant backslashes between brackets.
## Why is this bad?
Explicit line joins using a backslash are redundant between brackets.
## Example
```
x = (2 + \
    2)
```
## Use instead:
```
x = (2 +
    2)
```