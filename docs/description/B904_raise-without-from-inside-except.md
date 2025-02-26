# raise-without-from-inside-except (B904)
Derived from the flake8-bugbear linter.
## What it does
Checks for raise statements in exception handlers that lack a from
clause.
## Why is this bad?
In Python, raise can be used with or without an exception from which the
current exception is derived. This is known as exception chaining. When
printing the stack trace, chained exceptions are displayed in such a way
so as make it easier to trace the exception back to its root cause.
When raising an exception from within an except clause, always include a
from clause to facilitate exception chaining. If the exception is not
chained, it will be difficult to trace the exception back to its root cause.
## Example
```
try:
    ...
except FileNotFoundError:
    if ...:
        raise RuntimeError("...")
    else:
        raise UserWarning("...")
```
## Use instead:
```
try:
    ...
except FileNotFoundError as exc:
    if ...:
        raise RuntimeError("...") from None
    else:
        raise UserWarning("...") from exc
```