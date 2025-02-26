# duplicate-class-field-definition (PIE794)
Derived from the flake8-pie linter.
Fix is always available.
## What it does
Checks for duplicate field definitions in classes.
## Why is this bad?
Defining a field multiple times in a class body is redundant and likely a
mistake.
## Example
```
class Person:
    name = Tom
    ...
    name = Ben
```
## Use instead:
```
class Person:
    name = Tom
    ...
```