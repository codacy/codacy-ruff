# unnecessary-literal-set (C405)
Derived from the flake8-comprehensions linter.
Fix is always available.
## What it does
Checks for set() calls that take unnecessary list or tuple literals
as arguments.
## Why is this bad?
It's unnecessary to use a list or tuple literal within a call to set().
Instead, the expression can be rewritten as a set literal.
## Example
```
set([1, 2])
set((1, 2))
set([])
```
## Use instead:
```
{1, 2}
{1, 2}
set()
Fix safety
This rule's fix is marked as unsafe, as it may occasionally drop comments
when rewriting the call. In most cases, though, comments will be preserved.
```