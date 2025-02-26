# try-except-continue (S112)
Derived from the flake8-bandit linter.
## What it does
Checks for uses of the try-except-continue pattern.
## Why is this bad?
The try-except-continue pattern suppresses all exceptions.
Suppressing exceptions may hide errors that could otherwise reveal
unexpected behavior, security vulnerabilities, or malicious activity.
Instead, consider logging the exception.
## Example
```
import logging
while predicate:
    try:
        ...
    except Exception:
        continue
```
## Use instead:
```
import logging
while predicate:
    try:
        ...
    except Exception as exc:
        logging.exception("Error occurred")
```