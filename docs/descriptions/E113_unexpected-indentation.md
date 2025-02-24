# unexpected-indentation (E113)
Derived from the pycodestyle linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for unexpected indentation.
## Why is this bad?
Indentation outside of a code block is not valid Python syntax.
## Example
```
a = 1
    b = 2
```
## Use instead:
```
a = 1
b = 2
```