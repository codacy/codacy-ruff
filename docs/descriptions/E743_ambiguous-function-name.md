# ambiguous-function-name (E743)
Derived from the pycodestyle linter.
## What it does
Checks for the use of the characters 'l', 'O', or 'I' as function names.
## Why is this bad?
In some fonts, these characters are indistinguishable from the
numerals one and zero. When tempted to use 'l', use 'L' instead.
## Example
```
def l(x): ...
```
## Use instead:
```
def long_name(x): ...
```