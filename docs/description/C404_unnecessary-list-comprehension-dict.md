# unnecessary-list-comprehension-dict (C404)
Derived from the flake8-comprehensions linter.
Fix is always available.
## What it does
Checks for unnecessary list comprehensions.
## Why is this bad?
It's unnecessary to use a list comprehension inside a call to dict(),
since there is an equivalent comprehension for this type.
## Example
```
dict([(x, f(x)) for x in foo])
```
## Use instead:
```
{x: f(x) for x in foo}
Fix safety
This rule's fix is marked as unsafe, as it may occasionally drop comments
when rewriting the call. In most cases, though, comments will be preserved.
```