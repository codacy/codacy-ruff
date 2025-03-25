# unnecessary-collection-call (C408)
Derived from the flake8-comprehensions linter.
Fix is always available.
## What it does
Checks for unnecessary dict(), list() or tuple() calls that can be
rewritten as empty literals.
## Why is this bad?
It's unnecessary to call, e.g., dict() as opposed to using an empty
literal ({}). The former is slower because the name dict must be
looked up in the global scope in case it has been rebound.
## Example
```
dict()
dict(a=1, b=2)
list()
tuple()
```
## Use instead:
```
{}
{"a": 1, "b": 2}
[]
()
Fix safety
This rule's fix is marked as unsafe, as it may occasionally drop comments
when rewriting the call. In most cases, though, comments will be preserved.
```