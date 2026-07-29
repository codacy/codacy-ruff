# logging-eager-conversion (RUF065)
Preview (since 0.13.2) ·
Related issues ·
View source
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for eager string conversion of arguments to logging calls.
## Why is this bad?
Arguments to logging calls will be formatted as strings automatically, so it
is unnecessary and less efficient to eagerly format the arguments before passing
them in.
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
logging.info("%s - Something happened", str(user))
```
## Use instead:
```
import logging
logging.basicConfig(format="%(message)s", level=logging.INFO)
user = "Maria"
logging.info("%s - Something happened", user)
```