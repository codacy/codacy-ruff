# logging-percent-format (G002)
Derived from the flake8-logging-format linter.
## What it does
Checks for uses of printf-style format strings to format logging
messages.
## Why is this bad?
The logging module provides a mechanism for passing additional values to
be logged using the extra keyword argument. This is more consistent, more
efficient, and less error-prone than formatting the string directly.
Using printf-style format strings to format a logging message requires
that Python eagerly format the string, even if the logging statement is
never executed (e.g., if the log level is above the level of the logging
statement), whereas using the extra keyword argument defers formatting
until required.
Additionally, the use of extra will ensure that the values are made
available to all handlers, which can then be configured to log the values
in a consistent manner.
As an alternative to extra, passing values as arguments to the logging
method can also be used to defer string formatting until required.
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
logging.basicConfig(format="%(message)s", level=logging.INFO)
user = "Maria"
logging.info("%s - Something happened" % user)
```
## Use instead:
```
import logging
logging.basicConfig(format="%(user_id)s - %(message)s", level=logging.INFO)
user = "Maria"
logging.info("Something happened", extra=dict(user_id=user))
Or:
import logging
logging.basicConfig(format="%(message)s", level=logging.INFO)
user = "Maria"
logging.info("%s - Something happened", user)
```