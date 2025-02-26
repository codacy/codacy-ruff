# except-with-empty-tuple (B029)
Derived from the flake8-bugbear linter.
## What it does
Checks for exception handlers that catch an empty tuple.
## Why is this bad?
An exception handler that catches an empty tuple will not catch anything,
and is indicative of a mistake. Instead, add exceptions to the except
clause.
## Example
```
try:
    1 / 0
except ():
    ...
```
## Use instead:
```
try:
    1 / 0
except ZeroDivisionError:
    ...
```