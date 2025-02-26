# logging-exc-info (G201)
Derived from the flake8-logging-format linter.
## What it does
Checks for uses of logging.error that pass exc_info=True.
## Why is this bad?
Calling logging.error with exc_info=True is equivalent to calling
logging.exception. Using logging.exception is more concise, more
readable, and conveys the intent of the logging statement more clearly.
Known problems
This rule detects uses of the logging module via a heuristic.
Specifically, it matches against:
Uses of the logging module itself (e.g., import logging; logging.info(...)).
Uses of flask.current_app.logger (e.g., from flask import current_app; current_app.logger.info(...)).
Objects whose name starts with log or ends with logger or logging,
    when used in the same file in which they are defined (e.g., logger = logging.getLogger(); logger.info(...)).
Imported objects marked as loggers via the lint.logger-objects setting, which can be
    used to enforce these rules against shared logger objects (e.g., from module import logger; logger.info(...),
    when lint.logger-objects is set to ["module.logger"]).
## Example
```
import logging
try:
    ...
except ValueError:
    logging.error("Exception occurred", exc_info=True)
```
## Use instead:
```
import logging
try:
    ...
except ValueError:
    logging.exception("Exception occurred")
```