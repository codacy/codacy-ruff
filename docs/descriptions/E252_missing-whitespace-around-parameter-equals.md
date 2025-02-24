# missing-whitespace-around-parameter-equals (E252)
Derived from the pycodestyle linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for missing whitespace around the equals sign in an annotated
function keyword parameter.
## Why is this bad?
According to PEP 8, the spaces around the equals sign in a keyword
parameter should only be omitted when the parameter is unannotated:
Don’t use spaces around the = sign when used to indicate a keyword
argument, or when used to indicate a default value for an unannotated
function parameter.
## Example
```
def add(a: int=0) -> int:
    return a + 1
```
## Use instead:
```
def add(a: int = 0) -> int:
    return a + 1
```