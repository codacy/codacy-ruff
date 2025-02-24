# manual-list-copy (PERF402)
Derived from the Perflint linter.
## What it does
Checks for for loops that can be replaced by a making a copy of a list.
## Why is this bad?
When creating a copy of an existing list using a for-loop, prefer
list or list.copy instead. Making a direct copy is more readable and
more performant.
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