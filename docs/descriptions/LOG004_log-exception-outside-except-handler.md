# log-exception-outside-except-handler (LOG004)
Derived from the flake8-logging linter.
Fix is sometimes available.
This rule is unstable and in preview. The --preview flag is required for use.
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
Fix safety
The fix, if available, will always be marked as unsafe, as it changes runtime behavior.
```