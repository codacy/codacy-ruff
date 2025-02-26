# verbose-raise (TRY201)
Derived from the tryceratops linter.
Fix is always available.
## What it does
Checks for needless exception names in raise statements.
## Why is this bad?
It's redundant to specify the exception name in a raise statement if the
exception is being re-raised.
## Example
```
def foo():
    try:
        ...
    except ValueError as exc:
        raise exc
```
## Use instead:
```
def foo():
    try:
        ...
    except ValueError:
        raise
Fix safety
This rule's fix is marked as unsafe, as it doesn't properly handle bound
exceptions that are shadowed between the except and raise statements.
```