# root-logger-call (LOG015)
Derived from the flake8-logging linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for usages of the following logging top-level functions:
debug, info, warn, warning, error, critical, log, exception.
## Why is this bad?
Using the root logger causes the messages to have no source information,
making them less useful for debugging.
## Example
```
import logging
logging.info("Foobar")
```
## Use instead:
```
import logging
logger = logging.getLogger(__name__)
logger.info("Foobar")
```