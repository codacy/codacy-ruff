# unnecessary-list-call (C411)
Derived from the flake8-comprehensions linter.
Fix is always available.
## What it does
Checks for unnecessary list() calls around list comprehensions.
## Why is this bad?
It is redundant to use a list() call around a list comprehension.
## Examples
```
list([f(x) for x in foo])
Use instead
[f(x) for x in foo]
Fix safety
This rule's fix is marked as unsafe, as it may occasionally drop comments
when rewriting the call. In most cases, though, comments will be preserved.
```