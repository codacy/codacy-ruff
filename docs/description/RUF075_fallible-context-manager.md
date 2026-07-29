# fallible-context-manager (RUF075)
Preview (since 0.15.14) ·
Related issues ·
View source
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for @contextlib.contextmanager decorated functions that contain
yield expressions not protected against exceptions.
## Why is this bad?
When a context manager is used, code after yield is intended to run
during cleanup when the context exits. However, if an exception is raised
inside the with block, code after an unprotected yield will never
execute.
Wrapping yield in a try/finally or try/except block ensures
that exceptions are handled appropriately.
## Example
```
from contextlib import contextmanager
@contextmanager
def my_context():
    print("setup")
    yield
    print("cleanup")  # This won't run if an exception is raised!
```
## Use instead:
```
from contextlib import contextmanager
@contextmanager
def my_context():
    print("setup")
    try:
        yield
    finally:
        print("cleanup")  # This always runs
```