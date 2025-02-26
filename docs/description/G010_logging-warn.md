# logging-warn (G010)
Derived from the flake8-logging-format linter.
Fix is always available.
## What it does
Checks for uses of logging.warn and logging.Logger.warn.
## Why is this bad?
logging.warn and logging.Logger.warn are deprecated in favor of
logging.warning and logging.Logger.warning, which are functionally
equivalent.
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
logging.warn("Something happened")
```
## Use instead:
```
import logging
logging.warning("Something happened")
```