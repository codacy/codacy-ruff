# unnecessary-list-cast (PERF101)
Derived from the Perflint linter.
Fix is always available.
## What it does
Checks for explicit casts to list on for-loop iterables.
## Why is this bad?
Using a list() call to eagerly iterate over an already-iterable type
(like a tuple, list, or set) is inefficient, as it forces Python to create
a new list unnecessarily.
Removing the list() call will not change the behavior of the code, but
may improve performance.
Note that, as with all perflint rules, this is only intended as a
micro-optimization, and will have a negligible impact on performance in
most cases.
## Example
```
items = (1, 2, 3)
for i in list(items):
    print(i)
```
## Use instead:
```
items = (1, 2, 3)
for i in items:
    print(i)
```