# for-loop-set-mutations (FURB142)
Derived from the refurb linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for code that updates a set with the contents of an iterable by
using a for loop to call .add() or .discard() on each element
separately.
## Why is this bad?
When adding or removing a batch of elements to or from a set, it's more
idiomatic to use a single method call rather than adding or removing
elements one by one.
## Example
```
s = set()
for x in (1, 2, 3):
    s.add(x)
for x in (1, 2, 3):
    s.discard(x)
```
## Use instead:
```
s = set()
s.update((1, 2, 3))
s.difference_update((1, 2, 3))
Fix safety
The fix will be marked as unsafe if applying the fix would delete any comments.
Otherwise, it is marked as safe.
```