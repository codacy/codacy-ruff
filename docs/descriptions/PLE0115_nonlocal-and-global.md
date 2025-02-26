# nonlocal-and-global (PLE0115)
Derived from the Pylint linter.
## What it does
Checks for variables which are both declared as both nonlocal and
global.
## Why is this bad?
A nonlocal variable is a variable that is defined in the nearest
enclosing scope, but not in the global scope, while a global variable is
a variable that is defined in the global scope.
Declaring a variable as both nonlocal and global is contradictory and
will raise a SyntaxError.
## Example
```
counter = 0
def increment():
    global counter
    nonlocal counter
    counter += 1
```
## Use instead:
```
counter = 0
def increment():
    global counter
    counter += 1
```