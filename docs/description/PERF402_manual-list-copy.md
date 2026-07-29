# manual-list-copy (PERF402)
Added in v0.0.276 ·
Related issues ·
View source
Derived from the Perflint linter.
## What it does
Checks for for loops that append every item of an iterable to a list,
which can be replaced with a call to list.
## Why is this bad?
When populating a list from an iterable with a for loop, prefer list
instead. The list call is more readable and more performant. For an
existing list, you can also use list.copy instead of list.
Using the below as an example, the list-based copy is ~2x faster on
Python 3.11.
Note that, as with all perflint rules, this is only intended as a
micro-optimization, and will have a negligible impact on performance in
most cases.
## Example
```
original = list(range(10000))
filtered = []
for i in original:
    filtered.append(i)
```
## Use instead:
```
original = list(range(10000))
filtered = list(original)
```