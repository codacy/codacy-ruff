# return-in-try-except-finally (SIM107)
Derived from the flake8-simplify linter.
## What it does
Checks for return statements in try-except and finally blocks.
## Why is this bad?
The return statement in a finally block will always be executed, even if
an exception is raised in the try or except block. This can lead to
unexpected behavior.
## Example
```
def squared(n):
    try:
        sqr = n**2
        return sqr
    except Exception:
        return "An exception occurred"
    finally:
        return -1  # Always returns -1.
```
## Use instead:
```
def squared(n):
    try:
        return_value = n**2
    except Exception:
        return_value = "An exception occurred"
    finally:
        return_value = -1
    return return_value
```