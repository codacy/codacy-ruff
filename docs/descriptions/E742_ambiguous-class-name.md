# ambiguous-class-name (E742)
Derived from the pycodestyle linter.
## What it does
Checks for the use of the characters 'l', 'O', or 'I' as class names.
## Why is this bad?
In some fonts, these characters are indistinguishable from the
numerals one and zero. When tempted to use 'l', use 'L' instead.
## Example
```
class I(object): ...
```
## Use instead:
```
class Integer(object): ...
```