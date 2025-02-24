# boolean-chained-comparison (PLR1716)
Derived from the Pylint linter.
Fix is always available.
## What it does
Check for chained boolean operations that can be simplified.
## Why is this bad?
Refactoring the code will improve readability for these cases.
## Example
```
a = int(input())
b = int(input())
c = int(input())
if a < b and b < c:
    pass
```
## Use instead:
```
a = int(input())
b = int(input())
c = int(input())
if a < b < c:
    pass
```