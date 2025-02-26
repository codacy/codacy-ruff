# continue-outside-loop (F702)
Derived from the Pyflakes linter.
## What it does
Checks for continue statements outside of loops.
## Why is this bad?
The use of a continue statement outside of a for or while loop will
raise a SyntaxError.
## Example
```
def foo():
    continue  # SyntaxError
```