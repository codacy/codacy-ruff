# manual-dict-comprehension (PERF403)
Derived from the Perflint linter.
## What it does
Checks for for loops that can be replaced by a dictionary comprehension.
## Why is this bad?
When creating or extending a dictionary in a for-loop, prefer a dictionary
comprehension. Comprehensions are more readable and more performant.
For example, when comparing {x: x for x in list(range(1000))} to the for
loop version, the comprehension is ~10% faster on Python 3.11.
Note that, as with all perflint rules, this is only intended as a
micro-optimization, and will have a negligible impact on performance in
most cases.
## Example
```
pairs = (("a", 1), ("b", 2))
result = {}
for x, y in pairs:
    if y % 2:
        result[x] = y
```
## Use instead:
```
pairs = (("a", 1), ("b", 2))
result = {x: y for x, y in pairs if y % 2}
If you're appending to an existing dictionary, use the update method instead:
pairs = (("a", 1), ("b", 2))
result.update({x: y for x, y in pairs if y % 2})
```