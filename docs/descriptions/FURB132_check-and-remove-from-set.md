# check-and-remove-from-set (FURB132)
Derived from the refurb linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for uses of set.remove that can be replaced with set.discard.
## Why is this bad?
If an element should be removed from a set if it is present, it is more
succinct and idiomatic to use discard.
Known problems
This rule is prone to false negatives due to type inference limitations,
as it will only detect sets that are instantiated as literals or annotated
with a type annotation.
## Example
```
nums = {123, 456}
if 123 in nums:
    nums.remove(123)
```
## Use instead:
```
nums = {123, 456}
nums.discard(123)
```