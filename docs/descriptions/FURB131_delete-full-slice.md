# delete-full-slice (FURB131)
Derived from the refurb linter.
Fix is sometimes available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for del statements that delete the entire slice of a list or
dictionary.
## Why is this bad?
It is faster and more succinct to remove all items via the clear()
method.
Known problems
This rule is prone to false negatives due to type inference limitations,
as it will only detect lists and dictionaries that are instantiated as
literals or annotated with a type annotation.
## Example
```
names = {"key": "value"}
nums = [1, 2, 3]
del names[:]
del nums[:]
```
## Use instead:
```
names = {"key": "value"}
nums = [1, 2, 3]
names.clear()
nums.clear()
```