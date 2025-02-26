# undefined-local (F823)
Derived from the Pyflakes linter.
## What it does
Checks for undefined local variables.
## Why is this bad?
Referencing a local variable before it has been assigned will raise
an UnboundLocalError at runtime.
## Example
```
x = 1
def foo():
    x += 1
```
## Use instead:
```
x = 1
def foo():
    global x
    x += 1
```