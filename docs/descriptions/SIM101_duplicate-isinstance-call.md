# duplicate-isinstance-call (SIM101)
Derived from the flake8-simplify linter.
Fix is sometimes available.
## What it does
Checks for multiple isinstance calls on the same target.
## Why is this bad?
To check if an object is an instance of any one of multiple types
or classes, it is unnecessary to use multiple isinstance calls, as
the second argument of the isinstance built-in function accepts a
tuple of types and classes.
Using a single isinstance call implements the same behavior with more
concise code and clearer intent.
## Example
```
if isinstance(obj, int) or isinstance(obj, float):
    pass
```
## Use instead:
```
if isinstance(obj, (int, float)):
    pass
```