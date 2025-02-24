# except-with-non-exception-classes (B030)
Derived from the flake8-bugbear linter.
## What it does
Checks for exception handlers that catch non-exception classes.
## Why is this bad?
Catching classes that do not inherit from BaseException will raise a
TypeError.
## Example
```
try:
    1 / 0
except 1:
    ...
```
## Use instead:
```
try:
    1 / 0
except ZeroDivisionError:
    ...
```