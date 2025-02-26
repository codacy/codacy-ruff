# superfluous-else-break (RET508)
Derived from the flake8-return linter.
Fix is sometimes available.
## What it does
Checks for else statements with a break statement in the preceding if
block.
## Why is this bad?
The else statement is not needed, as the break statement will always
break out of the loop. Removing the else will reduce nesting and make the
code more readable.
## Example
```
def foo(bar, baz):
    for i in bar:
        if i > baz:
            break
        else:
            x = 0
```
## Use instead:
```
def foo(bar, baz):
    for i in bar:
        if i > baz:
            break
        x = 0
```