# logging-config-insecure-listen (S612)
Derived from the flake8-bandit linter.
## What it does
Checks for insecure logging.config.listen calls.
## Why is this bad?
logging.config.listen starts a server that listens for logging
configuration requests. This is insecure, as parts of the configuration are
passed to the built-in eval function, which can be used to execute
arbitrary code.
## Example
```
import logging
logging.config.listen(9999)
```