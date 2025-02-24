# global-variable-not-assigned (PLW0602)
Derived from the Pylint linter.
## What it does
Checks for global variables that are not assigned a value in the current
scope.
## Why is this bad?
The global keyword allows an inner scope to modify a variable declared
in the outer scope. If the variable is not modified within the inner scope,
there is no need to use global.
## Example
```
DEBUG = True
def foo():
    global DEBUG
    if DEBUG:
        print("foo() called")
    ...
```
## Use instead:
```
DEBUG = True
def foo():
    if DEBUG:
        print("foo() called")
    ...
```