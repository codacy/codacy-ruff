# raise-without-from-inside-except (B904)
Added in v0.0.138 ·
Related issues ·
View source
Derived from the flake8-bugbear linter.
## What it does
Checks for raise statements in exception handlers that lack a from
clause.
## Why is this bad?
In Python, raise can be used with or without an exception from which the
current exception is derived. This is known as exception chaining. When
printing the stack trace, chained exceptions are displayed in such a way
so as make it easier to trace the exception back to its root cause.
When raising a new exception from within an except clause, it's recommended to
include a from clause to explicitly set the exception's cause. Without it,
Python will implicitly chain from the current exception (setting __context__),
but the __cause__ attribute won't be set, which may make debugging slightly
more difficult.
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