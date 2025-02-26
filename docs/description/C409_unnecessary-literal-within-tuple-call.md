# unnecessary-literal-within-tuple-call (C409)
Derived from the flake8-comprehensions linter.
Fix is always available.
## What it does
Checks for tuple calls that take unnecessary list or tuple literals as
arguments. In preview, this also includes unnecessary list comprehensions
within tuple calls.
## Why is this bad?
It's unnecessary to use a list or tuple literal within a tuple() call,
since there is a literal syntax for these types.
If a list literal was passed, then it should be rewritten as a tuple
literal. Otherwise, if a tuple literal was passed, then the outer call
to tuple() should be removed.
In preview, this rule also checks for list comprehensions within tuple()
calls. If a list comprehension is found, it should be rewritten as a
generator expression.
## Examples
```
tuple([1, 2])
tuple((1, 2))
tuple([x for x in range(10)])
```
## Use instead:
```
(1, 2)
(1, 2)
tuple(x for x in range(10))
Fix safety
This rule's fix is marked as unsafe, as it may occasionally drop comments
when rewriting the call. In most cases, though, comments will be preserved.
```