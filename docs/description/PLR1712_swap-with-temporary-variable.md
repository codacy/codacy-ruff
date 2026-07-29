# swap-with-temporary-variable (PLR1712)
Preview (since 0.15.3) ·
Related issues ·
View source
Derived from the Pylint linter.
Fix is sometimes available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for code that swaps two variables using a temporary variable.
## Why is this bad?
Variables can be swapped by using tuple unpacking instead of using a
temporary variable. That also makes the intention of the swapping logic
more clear.
## Example
```
def function(x, y):
    if x > y:
        temp = x
        x = y
        y = temp
    assert x <= y
```
## Use instead:
```
def function(x, y):
    if x > y:
        x, y = y, x
    assert x <= y
Fix safety
The rule's fix is marked as safe, unless the replacement range contains comments
that would be removed.
```