# jump-statement-in-finally (B012)
Derived from the flake8-bugbear linter.
## What it does
Checks for break, continue, and return statements in finally
blocks.
## Why is this bad?
The use of break, continue, and return statements in finally blocks
can cause exceptions to be silenced.
finally blocks execute regardless of whether an exception is raised. If a
break, continue, or return statement is reached in a finally block,
any exception raised in the try or except blocks will be silenced.
## Example
```
def speed(distance, time):
    try:
        return distance / time
    except ZeroDivisionError:
        raise ValueError("Time cannot be zero")
    finally:
        return 299792458  # `ValueError` is silenced
```
## Use instead:
```
def speed(distance, time):
    try:
        return distance / time
    except ZeroDivisionError:
        raise ValueError("Time cannot be zero")
```