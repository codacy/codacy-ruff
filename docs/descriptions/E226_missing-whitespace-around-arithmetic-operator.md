# missing-whitespace-around-arithmetic-operator (E226)
Derived from the pycodestyle linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for missing whitespace arithmetic operators.
## Why is this bad?
According to PEP 8, there should be one space before and after an
arithmetic operator (+, -, /, and *).
## Example
```
number = 40+2
```
## Use instead:
```
number = 40 + 2
```