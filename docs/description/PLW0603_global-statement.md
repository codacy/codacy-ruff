# global-statement (PLW0603)
Derived from the Pylint linter.
## What it does
Checks for the use of global statements to update identifiers.
## Why is this bad?
Pylint discourages the use of global variables as global mutable
state is a common source of bugs and confusing behavior.
## Example
```
var = 1
def foo():
    global var  # [global-statement]
    var = 10
    print(var)
foo()
print(var)
```
## Use instead:
```
var = 1
def foo():
    print(var)
    return 10
var = foo()
print(var)
```