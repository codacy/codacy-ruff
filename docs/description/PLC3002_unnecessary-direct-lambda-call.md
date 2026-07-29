# unnecessary-direct-lambda-call (PLC3002)
Added in v0.0.153 ·
Related issues ·
View source
Derived from the Pylint linter.
## What it does
Checks for unnecessary direct calls to lambda expressions.
## Why is this bad?
Calling a lambda expression directly is unnecessary. The expression can be
executed inline instead to improve readability.
## Example
```
area = (lambda r: 3.14 * r**2)(radius)
```
## Use instead:
```
area = 3.14 * radius**2
```