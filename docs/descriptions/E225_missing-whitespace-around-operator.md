# missing-whitespace-around-operator (E225)
Derived from the pycodestyle linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for missing whitespace around all operators.
## Why is this bad?
According to PEP 8, there should be one space before and after all
operators.
## Example
```
if number==42:
    print('you have found the meaning of life')
```
## Use instead:
```
if number == 42:
    print('you have found the meaning of life')
```