# useless-try-except (TRY203)
Added in 0.7.0 ·
Related issues ·
View source
Derived from the tryceratops linter.
## What it does
Checks for immediate uses of raise within exception handlers.
## Why is this bad?
Capturing an exception, only to immediately reraise it, has no effect.
Instead, remove the error-handling code and let the exception propagate
upwards without the unnecessary try-except block.
## Example
```
def foo():
    try:
        bar()
    except NotImplementedError:
        raise
```
## Use instead:
```
def foo():
    bar()
```