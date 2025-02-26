# undocumented-warn (LOG009)
Derived from the flake8-logging linter.
Fix is sometimes available.
## What it does
Checks for uses of logging.WARN.
## Why is this bad?
The logging.WARN constant is an undocumented alias for logging.WARNING.
Although it’s not explicitly deprecated, logging.WARN is not mentioned
in the logging documentation. Prefer logging.WARNING instead.
## Example
```
import logging
logging.basicConfig(level=logging.WARN)
```
## Use instead:
```
import logging
logging.basicConfig(level=logging.WARNING)
```