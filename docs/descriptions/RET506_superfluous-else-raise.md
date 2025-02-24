# superfluous-else-raise (RET506)
Derived from the flake8-return linter.
Fix is sometimes available.
## What it does
Checks for else statements with a raise statement in the preceding if
block.
## Why is this bad?
The else statement is not needed as the raise statement will always
break out of the current scope. Removing the else will reduce nesting
and make the code more readable.
## Example
```
def foo(bar, baz):
    if bar == "Specific Error":
        raise Exception(bar)
    else:
        raise Exception(baz)
```
## Use instead:
```
def foo(bar, baz):
    if bar == "Specific Error":
        raise Exception(bar)
    raise Exception(baz)
```