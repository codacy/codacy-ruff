# zip-without-explicit-strict (B905)
Derived from the flake8-bugbear linter.
Fix is always available.
## What it does
Checks for zip calls without an explicit strict parameter.
## Why is this bad?
By default, if the iterables passed to zip are of different lengths, the
resulting iterator will be silently truncated to the length of the shortest
iterable. This can lead to subtle bugs.
Pass strict=True to raise a ValueError if the iterables are of
non-uniform length. Alternatively, if the iterables are deliberately of
different lengths, pass strict=False to make the intention explicit.
## Example
```
zip(a, b)
```
## Use instead:
```
zip(a, b, strict=True)
Fix safety
This rule's fix is marked as unsafe for zip calls that contain
**kwargs, as adding a strict keyword argument to such a call may lead
to a duplicate keyword argument error.
```