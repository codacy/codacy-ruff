# literal-membership (PLR6201)
Preview (since v0.1.1) ·
Related issues ·
View source
Derived from the Pylint linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for membership tests on list and tuple literals.
## Why is this bad?
When testing for membership in a static sequence, prefer a set literal
over a list or tuple, as Python optimizes set membership tests.
## Example
```
1 in [1, 2, 3]
```
## Use instead:
```
1 in {1, 2, 3}
Fix safety
This rule's fix is marked as unsafe, as the use of a set literal will
error at runtime if either the element being tested for membership (the
left-hand side) or any element of the sequence (the right-hand side)
is unhashable (like lists or dictionaries). While Ruff will attempt to
infer the hashability of both sides and skip the fix when it can determine
that either side is unhashable, it may not always be able to do so.
```