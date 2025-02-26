# blind-except (BLE001)
Derived from the flake8-blind-except linter.
## What it does
Checks for except clauses that catch all exceptions. This includes
bare except, except BaseException and except Exception.
## Why is this bad?
Overly broad except clauses can lead to unexpected behavior, such as
catching KeyboardInterrupt or SystemExit exceptions that prevent the
user from exiting the program.
Instead of catching all exceptions, catch only those that are expected to
be raised in the try block.
## Example
```
try:
    foo()
except BaseException:
    ...
```
## Use instead:
```
try:
    foo()
except FileNotFoundError:
    ...
Exceptions that are re-raised will not be flagged, as they're expected to
be caught elsewhere:
try:
    foo()
except BaseException:
    raise
Exceptions that are logged via logging.exception() or logging.error()
with exc_info enabled will not be flagged, as this is a common pattern
for propagating exception traces:
try:
    foo()
except BaseException:
    logging.exception("Something went wrong")
```