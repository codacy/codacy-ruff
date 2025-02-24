# multiple-spaces-after-comma (E241)
Derived from the pycodestyle linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for extraneous whitespace after a comma.
## Why is this bad?
Consistency is good. This rule helps ensure you have a consistent
formatting style across your project.
## Example
```
a = 4,    5
```
## Use instead:
```
a = 4, 5
```