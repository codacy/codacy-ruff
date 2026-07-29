# missing-whitespace-around-operator (E225)
Preview (since v0.0.269) ·
Related issues ·
View source
Derived from the pycodestyle linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for missing whitespace around all operators.
## Why is this bad?
According to PEP 8, there should be one space before and after all
assignment (=), augmented assignment (+=, -=, etc.), comparison,
and Booleans operators.
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