# direct-logger-instantiation (LOG001)
Derived from the flake8-logging linter.
Fix is sometimes available.
## What it does
Checks for direct instantiation of logging.Logger, as opposed to using
logging.getLogger().
## Why is this bad?
The Logger Objects documentation states that:
Note that Loggers should NEVER be instantiated directly, but always
through the module-level function logging.getLogger(name).
If a logger is directly instantiated, it won't be added to the logger
tree, and will bypass all configuration. Messages logged to it will
only be sent to the "handler of last resort", skipping any filtering
or formatting.
## Example
```
import logging
logger = logging.Logger(__name__)
```
## Use instead:
```
import logging
logger = logging.getLogger(__name__)
```