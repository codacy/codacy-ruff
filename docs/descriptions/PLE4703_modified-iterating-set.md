# modified-iterating-set (PLE4703)
Derived from the Pylint linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for loops in which a set is modified during iteration.
## Why is this bad?
If a set is modified during iteration, it will cause a RuntimeError.
If you need to modify a set within a loop, consider iterating over a copy
of the set instead.
Known problems
This rule favors false negatives over false positives. Specifically, it
will only detect variables that can be inferred to be a set type based on
local type inference, and will only detect modifications that are made
directly on the variable itself (e.g., set.add()), as opposed to
modifications within other function calls (e.g., some_function(set)).
## Example
```
nums = {1, 2, 3}
for num in nums:
    nums.add(num + 5)
```
## Use instead:
```
nums = {1, 2, 3}
for num in nums.copy():
    nums.add(num + 5)
```