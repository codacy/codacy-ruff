# superfluous-else-continue (RET507)
Derived from the flake8-return linter.
Fix is sometimes available.
## What it does
Checks for else statements with a continue statement in the preceding
if block.
## Why is this bad?
The else statement is not needed, as the continue statement will always
continue onto the next iteration of a loop. Removing the else will reduce
nesting and make the code more readable.
## Example
```
def foo(bar, baz):
    for i in bar:
        if i < baz:
            continue
        else:
            x = 0
```
## Use instead:
```
def foo(bar, baz):
    for i in bar:
        if i < baz:
            continue
        x = 0
```