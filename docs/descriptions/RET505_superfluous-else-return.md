# superfluous-else-return (RET505)
Derived from the flake8-return linter.
Fix is sometimes available.
## What it does
Checks for else statements with a return statement in the preceding
if block.
## Why is this bad?
The else statement is not needed as the return statement will always
break out of the enclosing function. Removing the else will reduce
nesting and make the code more readable.
## Example
```
def foo(bar, baz):
    if bar:
        return 1
    else:
        return baz
```
## Use instead:
```
def foo(bar, baz):
    if bar:
        return 1
    return baz
```