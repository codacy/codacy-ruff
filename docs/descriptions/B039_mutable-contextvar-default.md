# mutable-contextvar-default (B039)
Derived from the flake8-bugbear linter.
## What it does
Checks for uses of mutable objects as ContextVar defaults.
## Why is this bad?
The ContextVar default is evaluated once, when the ContextVar is defined.
The same mutable object is then shared across all .get() method calls to
the ContextVar. If the object is modified, those modifications will persist
across calls, which can lead to unexpected behavior.
Instead, prefer to use immutable data structures. Alternatively, take
None as a default, and initialize a new mutable object inside for each
call using the .set() method.
Types outside the standard library can be marked as immutable with the
lint.flake8-bugbear.extend-immutable-calls configuration option.
## Example
```
from contextvars import ContextVar
cv: ContextVar[list] = ContextVar("cv", default=[])
```
## Use instead:
```
from contextvars import ContextVar
cv: ContextVar[list | None] = ContextVar("cv", default=None)
...
if cv.get() is None:
    cv.set([])
```