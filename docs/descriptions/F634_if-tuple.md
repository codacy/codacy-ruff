# if-tuple (F634)
Derived from the Pyflakes linter.
## What it does
Checks for if statements that use non-empty tuples as test conditions.
## Why is this bad?
Non-empty tuples are always True, so an if statement with a non-empty
tuple as its test condition will always pass. This is likely a mistake.
## Example
```
if (False,):
    print("This will always run")
```
## Use instead:
```
if False:
    print("This will never run")
```