# unnecessary-call-around-sorted (C413)
Derived from the flake8-comprehensions linter.
Fix is always available.
## What it does
Checks for unnecessary list() or reversed() calls around sorted()
calls.
## Why is this bad?
It is unnecessary to use list() around sorted(), as the latter already
returns a list.
It is also unnecessary to use reversed() around sorted(), as the latter
has a reverse argument that can be used in lieu of an additional
reversed() call.
In both cases, it's clearer and more efficient to avoid the redundant call.
## Examples
```
reversed(sorted(iterable))
```
## Use instead:
```
sorted(iterable, reverse=True)
Fix safety
This rule's fix is marked as unsafe, as reversed() and reverse=True will
yield different results in the event of custom sort keys or equality
functions. Specifically, reversed() will reverse the order of the
collection, while sorted() with reverse=True will perform a stable
reverse sort, which will preserve the order of elements that compare as
equal.
```