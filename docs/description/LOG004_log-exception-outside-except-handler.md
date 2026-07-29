# log-exception-outside-except-handler (LOG004)
Added in 0.16.0 ·
Related issues ·
View source
Derived from the flake8-logging linter.
Fix is sometimes available.
## What it does
Checks for .exception() logging calls outside of exception handlers.
## Why is this bad?
The documentation states:
This function should only be called from an exception handler.
Calling .exception() outside of an exception handler
attaches None as exception information, leading to confusing messages:
>>> logging.exception("example")
ERROR:root:example
NoneType: None
## Example
```
import logging
logging.exception("Foobar")
```
## Use instead:
```
import logging
logging.error("Foobar")
Known limitations
This rule checks whether a call is defined inside an exception handler, not
whether it executes inside one. A function defined in an except block but
called outside of it will not be flagged, despite the fact that the call may
not have access to an active exception at runtime:
import logging
try:
    raise ValueError()
except Exception:
    def handler():
        logging.exception("Foobar")  # LOG004 not raised (false negative)
handler()
Fix safety
The fix, if available, will always be marked as unsafe, as it changes runtime behavior.
```