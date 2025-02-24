# tab-after-operator (E224)
Derived from the pycodestyle linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for extraneous tabs after an operator.
## Why is this bad?
According to PEP 8, operators should be surrounded by at most a single space on either
side.
## Example
```
a = 4 +\t5
```
## Use instead:
```
a = 4 + 5
```