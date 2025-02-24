# duplicate-handler-exception (B014)
Derived from the flake8-bugbear linter.
Fix is always available.
## What it does
Checks for exception handlers that catch duplicate exceptions.
## Why is this bad?
Including the same exception multiple times in the same handler is redundant,
as the first exception will catch the exception, making the second exception
unreachable. The same applies to exception hierarchies, as a handler for a
parent exception (like Exception) will also catch child exceptions (like
ValueError).
## Example
```
try:
    ...
except (Exception, ValueError):  # `Exception` includes `ValueError`.
    ...
```
## Use instead:
```
try:
    ...
except Exception:
    ...
```