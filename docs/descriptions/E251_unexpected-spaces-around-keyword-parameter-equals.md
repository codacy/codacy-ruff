# unexpected-spaces-around-keyword-parameter-equals (E251)
Derived from the pycodestyle linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for missing whitespace around the equals sign in an unannotated
function keyword parameter.
## Why is this bad?
According to PEP 8, there should be no spaces around the equals sign in a
keyword parameter, if it is unannotated:
Don’t use spaces around the = sign when used to indicate a keyword
argument, or when used to indicate a default value for an unannotated
function parameter.
## Example
```
def add(a = 0) -> int:
    return a + 1
```
## Use instead:
```
def add(a=0) -> int:
    return a + 1
```