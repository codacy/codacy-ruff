# logging-extra-attr-clash (G101)
Derived from the flake8-logging-format linter.
## What it does
Checks for extra keywords in logging statements that clash with
LogRecord attributes.
## Why is this bad?
The logging module provides a mechanism for passing additional values to
be logged using the extra keyword argument. These values are then passed
to the LogRecord constructor.
Providing a value via extra that clashes with one of the attributes of
the LogRecord constructor will raise a KeyError when the LogRecord is
constructed.
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
logging.basicConfig(format="%(name) - %(message)s", level=logging.INFO)
username = "Maria"
logging.info("Something happened", extra=dict(name=username))
```
## Use instead:
```
import logging
logging.basicConfig(format="%(user_id)s - %(message)s", level=logging.INFO)
username = "Maria"
logging.info("Something happened", extra=dict(user_id=username))
```