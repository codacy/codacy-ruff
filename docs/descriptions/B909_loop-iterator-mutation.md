# loop-iterator-mutation (B909)
Derived from the flake8-bugbear linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for mutations to an iterable during a loop iteration.
## Why is this bad?
When iterating over an iterable, mutating the iterable can lead to unexpected
behavior, like skipping elements or infinite loops.
## Example
```
items = [1, 2, 3]
for item in items:
    print(item)
    # Create an infinite loop by appending to the list.
    items.append(item)
```