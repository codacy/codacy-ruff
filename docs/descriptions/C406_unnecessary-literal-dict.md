# unnecessary-literal-dict (C406)
Derived from the flake8-comprehensions linter.
Fix is always available.
## What it does
Checks for unnecessary list or tuple literals.
## Why is this bad?
It's unnecessary to use a list or tuple literal within a call to dict().
It can be rewritten as a dict literal ({}).
## Examples
```
dict([(1, 2), (3, 4)])
dict(((1, 2), (3, 4)))
dict([])
```
## Use instead:
```
{1: 2, 3: 4}
{1: 2, 3: 4}
{}
Fix safety
This rule's fix is marked as unsafe, as it may occasionally drop comments
when rewriting the call. In most cases, though, comments will be preserved.
```