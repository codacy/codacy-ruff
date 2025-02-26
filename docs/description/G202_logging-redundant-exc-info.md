# logging-redundant-exc-info (G202)
Derived from the flake8-logging-format linter.
## What it does
Checks for redundant exc_info keyword arguments in logging statements.
## Why is this bad?
exc_info is True by default for logging.exception, and False by
default for logging.error.
Passing exc_info=True to logging.exception calls is redundant, as is
passing exc_info=False to logging.error calls.
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
    logging.exception("Exception occurred", exc_info=True)
```
## Use instead:
```
import logging
try:
    ...
except ValueError:
    logging.exception("Exception occurred")
```