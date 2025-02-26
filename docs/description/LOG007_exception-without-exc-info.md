# exception-without-exc-info (LOG007)
Derived from the flake8-logging linter.
## What it does
Checks for uses of logging.exception() with exc_info set to False.
## Why is this bad?
The logging.exception() method captures the exception automatically, but
accepts an optional exc_info argument to override this behavior. Setting
exc_info to False disables the automatic capture of the exception and
stack trace.
Instead of setting exc_info to False, prefer logging.error(), which
has equivalent behavior to logging.exception() with exc_info set to
False, but is clearer in intent.
## Example
```
logging.exception("...", exc_info=False)
```
## Use instead:
```
logging.error("...")
```