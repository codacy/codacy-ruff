# binary-op-exception (PLW0711)
Derived from the Pylint linter.
## What it does
Checks for except clauses that attempt to catch multiple
exceptions with a binary operation (and or or).
## Why is this bad?
A binary operation will not catch multiple exceptions. Instead, the binary
operation will be evaluated first, and the result of that operation will
be caught (for an or operation, this is typically the first exception in
the list). This is almost never the desired behavior.
## Example
```
try:
    pass
except A or B:
    pass
```
## Use instead:
```
try:
    pass
except (A, B):
    pass
```