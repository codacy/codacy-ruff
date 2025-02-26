# list-reverse-copy (FURB187)
Derived from the refurb linter.
Fix is always available.
## What it does
Checks for list reversals that can be performed in-place in lieu of
creating a new list.
## Why is this bad?
When reversing a list, it's more efficient to use the in-place method
.reverse() instead of creating a new list, if the original list is
no longer needed.
## Example
```
l = [1, 2, 3]
l = reversed(l)
l = [1, 2, 3]
l = list(reversed(l))
l = [1, 2, 3]
l = l[::-1]
```
## Use instead:
```
l = [1, 2, 3]
l.reverse()
Fix safety
This rule's fix is marked as unsafe, as calling .reverse() on a list
will mutate the list in-place, unlike reversed, which creates a new list
and leaves the original list unchanged.
If the list is referenced elsewhere, this could lead to unexpected
behavior.
```