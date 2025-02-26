# break-outside-loop (F701)
Derived from the Pyflakes linter.
## What it does
Checks for break statements outside of loops.
## Why is this bad?
The use of a break statement outside of a for or while loop will
raise a SyntaxError.
## Example
```
def foo():
    break
```