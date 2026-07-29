# exc-info-outside-except-handler (LOG014)
Added in 0.12.0 ·
Related issues ·
View source
Derived from the flake8-logging linter.
Fix is sometimes available.
## What it does
Checks for logging calls with exc_info= outside exception handlers.
## Why is this bad?
Using exc_info=True outside of an exception handler
attaches None as the exception information, leading to confusing messages:
>>> logging.warning("Uh oh", exc_info=True)
WARNING:root:Uh oh
NoneType: None
## Example
```
import logging
logging.warning("Foobar", exc_info=True)
```
## Use instead:
```
import logging
logging.warning("Foobar")
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
        logging.error("Foobar", exc_info=True)  # LOG014 not raised (false negative)
handler()
Fix safety
The fix is always marked as unsafe, as it changes runtime behavior.
```