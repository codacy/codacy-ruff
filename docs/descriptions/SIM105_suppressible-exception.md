# suppressible-exception (SIM105)
Derived from the flake8-simplify linter.
Fix is sometimes available.
## What it does
Checks for try-except-pass blocks that can be replaced with the
contextlib.suppress context manager.
## Why is this bad?
Using contextlib.suppress is more concise and directly communicates the
intent of the code: to suppress a given exception.
Note that contextlib.suppress is slower than using try-except-pass
directly. For performance-critical code, consider retaining the
try-except-pass pattern.
## Example
```
try:
    1 / 0
except ZeroDivisionError:
    pass
```
## Use instead:
```
import contextlib
with contextlib.suppress(ZeroDivisionError):
    1 / 0
```