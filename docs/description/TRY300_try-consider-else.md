# try-consider-else (TRY300)
Derived from the tryceratops linter.
## What it does
Checks for return statements in try blocks.
## Why is this bad?
The try-except statement has an else clause for code that should
run only if no exceptions were raised. Returns in try blocks may
exhibit confusing or unwanted behavior, such as being overridden by
control flow in except and finally blocks, or unintentionally
suppressing an exception.
## Example
```
import logging
def reciprocal(n):
    try:
        rec = 1 / n
        print(f"reciprocal of {n} is {rec}")
        return rec
    except ZeroDivisionError:
        logging.exception("Exception occurred")
```
## Use instead:
```
import logging
def reciprocal(n):
    try:
        rec = 1 / n
    except ZeroDivisionError:
        logging.exception("Exception occurred")
    else:
        print(f"reciprocal of {n} is {rec}")
        return rec
```