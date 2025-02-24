# logging-too-many-args (PLE1205)
Derived from the Pylint linter.
## What it does
Checks for too many positional arguments for a logging format string.
## Why is this bad?
A TypeError will be raised if the statement is run.
## Example
```
import logging
try:
    function()
except Exception as e:
    logging.error("Error occurred: %s", type(e), e)
    raise
```
## Use instead:
```
import logging
try:
    function()
except Exception as e:
    logging.error("%s error occurred: %s", type(e), e)
    raise
```