# unnecessary-literal-within-list-call (C410)
Derived from the flake8-comprehensions linter.
Fix is always available.
## What it does
Checks for list() calls that take unnecessary list or tuple literals as
arguments.
## Why is this bad?
It's unnecessary to use a list or tuple literal within a list() call,
since there is a literal syntax for these types.
If a list literal is passed in, then the outer call to list() should be
removed. Otherwise, if a tuple literal is passed in, then it should be
rewritten as a list literal.
## Examples
```
list([1, 2])
list((1, 2))
```
## Use instead:
```
[1, 2]
[1, 2]
Fix safety
This rule's fix is marked as unsafe, as it may occasionally drop comments
when rewriting the call. In most cases, though, comments will be preserved.
```