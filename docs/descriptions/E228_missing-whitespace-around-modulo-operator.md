# missing-whitespace-around-modulo-operator (E228)
Derived from the pycodestyle linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for missing whitespace around the modulo operator.
## Why is this bad?
According to PEP 8, the modulo operator (%) should have whitespace on
either side of it.
## Example
```
remainder = 10%2
```
## Use instead:
```
remainder = 10 % 2
```