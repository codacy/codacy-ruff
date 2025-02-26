# verbose-log-message (TRY401)
Derived from the tryceratops linter.
## What it does
Checks for excessive logging of exception objects.
## Why is this bad?
When logging exceptions via logging.exception, the exception object
is logged automatically. Including the exception object in the log
message is redundant and can lead to excessive logging.
## Example
```
try:
    ...
except ValueError as e:
    logger.exception(f"Found an error: {e}")
```
## Use instead:
```
try:
    ...
except ValueError:
    logger.exception("Found an error")
```