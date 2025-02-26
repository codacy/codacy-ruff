# try-except-pass (S110)
Derived from the flake8-bandit linter.
## What it does
Checks for uses of the try-except-pass pattern.
## Why is this bad?
The try-except-pass pattern suppresses all exceptions. Suppressing
exceptions may hide errors that could otherwise reveal unexpected behavior,
security vulnerabilities, or malicious activity. Instead, consider logging
the exception.
## Example
```
try:
    ...
except Exception:
    pass
```
## Use instead:
```
import logging
try:
    ...
except Exception as exc:
    logging.exception("Exception occurred")
```