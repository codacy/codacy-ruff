# exc-info-outside-except-handler (LOG014)
Derived from the flake8-logging linter.
Fix is sometimes available.
This rule is unstable and in preview. The --preview flag is required for use.
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
Fix safety
The fix is always marked as unsafe, as it changes runtime behavior.
```