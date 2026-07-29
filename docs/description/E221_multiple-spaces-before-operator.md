# multiple-spaces-before-operator (E221)
Preview (since v0.0.269) ·
Related issues ·
View source
Derived from the pycodestyle linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for extraneous whitespace before an operator.
## Why is this bad?
According to PEP 8, operators should be surrounded by at most a single space on either
side.
## Example
```
a = 4  + 5
```
## Use instead:
```
a = 4 + 5
```