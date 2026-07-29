# logging-too-few-args (PLE1206)
Added in v0.0.252 ·
Related issues ·
View source
Derived from the Pylint linter.
## What it does
Checks for too few positional arguments for a logging format string.
## Why is this bad?
A TypeError will be raised if the statement is run.
## Example
```
import logging
try:
    function()
except Exception as e:
    logging.error("%s error occurred: %s", e)
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