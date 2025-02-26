# error-instead-of-exception (TRY400)
Derived from the tryceratops linter.
Fix is sometimes available.
## What it does
Checks for uses of logging.error instead of logging.exception when
logging an exception.
## Why is this bad?
logging.exception logs the exception and the traceback, while
logging.error only logs the exception. The former is more appropriate
when logging an exception, as the traceback is often useful for debugging.
## Example
```
import logging
def func():
    try:
        raise NotImplementedError
    except NotImplementedError:
        logging.error("Exception occurred")
```
## Use instead:
```
import logging
def func():
    try:
        raise NotImplementedError
    except NotImplementedError:
        logging.exception("Exception occurred")
Fix safety
This rule's fix is marked as safe when run against logging.error calls,
but unsafe when marked against other logger-like calls (e.g.,
logger.error), since the rule is prone to false positives when detecting
logger-like calls outside of the logging module.
```