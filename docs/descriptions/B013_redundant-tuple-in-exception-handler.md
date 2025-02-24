# redundant-tuple-in-exception-handler (B013)
Derived from the flake8-bugbear linter.
Fix is always available.
## What it does
Checks for single-element tuples in exception handlers (e.g.,
except (ValueError,):).
Note: Single-element tuples consisting of a starred expression
are allowed.
## Why is this bad?
A tuple with a single element can be more concisely and idiomatically
expressed as a single value.
## Example
```
try:
    ...
except (ValueError,):
    ...
```
## Use instead:
```
try:
    ...
except ValueError:
    ...
```