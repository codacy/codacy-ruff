# non-pep604-isinstance (UP038)
Derived from the pyupgrade linter.
Fix is always available.
## What it does
Checks for uses of isinstance and issubclass that take a tuple
of types for comparison.
## Why is this bad?
Since Python 3.10, isinstance and issubclass can be passed a
|-separated union of types, which is consistent
with the union operator introduced in PEP 604.
Note that this results in slower code. Ignore this rule if the
performance of an isinstance or issubclass check is a
concern, e.g., in a hot loop.
## Example
```
isinstance(x, (int, float))
```
## Use instead:
```
isinstance(x, int | float)
```